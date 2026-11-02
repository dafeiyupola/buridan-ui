"""Direct tests for ``patch_rxconfig`` (``cli/main.py``).

``patch_rxconfig`` injects Buridan UI's ``TailwindV4Plugin`` config into a
user's ``rxconfig.py`` via an AST-based pass (``_inject_via_ast``) with a
naive string-replace fallback (``_append_plugins_fallback``). It previously
had no direct tests — only exercised indirectly through ``cmd_init`` — so a
regression in any of the AST branches, the fallback, or the early-return/
warning paths could go unnoticed. See issue #246.
"""  # noqa: INP001

import ast
from pathlib import Path

import pytest

from cli.main import cmd_init, patch_rxconfig


def _write_config(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "rxconfig.py"
    path.write_text(content, encoding="utf-8")
    return path


# ── fresh config: no plugins kwarg yet ──────────────────────────────────────


def test_patches_fresh_config_without_plugins_kwarg(tmp_path: Path) -> None:
    path = _write_config(
        tmp_path,
        'import reflex as rx\n\nconfig = rx.Config(app_name="t")\n',
    )
    patch_rxconfig(path)
    patched = path.read_text(encoding="utf-8")

    assert "from reflex.plugins.shared_tailwind import TailwindConfig" in patched
    assert "TailwindV4Plugin(" in patched
    assert "var(--background)" in patched
    ast.parse(patched)


# ── idempotence: a second run is a no-op early return ───────────────────────


def test_second_run_is_idempotent_and_leaves_file_byte_identical(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    path = _write_config(
        tmp_path,
        'import reflex as rx\n\nconfig = rx.Config(app_name="t")\n',
    )
    patch_rxconfig(path)
    first = path.read_text(encoding="utf-8")

    patch_rxconfig(path)
    second = path.read_text(encoding="utf-8")

    assert second == first
    assert "already contains Buridan UI theme tokens" in capsys.readouterr().out


# ── AST pass: existing plugins=[...] list is merged, not replaced ──────────


def test_merges_into_existing_empty_plugins_list(tmp_path: Path) -> None:
    path = _write_config(
        tmp_path,
        'import reflex as rx\n\nconfig = rx.Config(app_name="t", plugins=[])\n',
    )
    patch_rxconfig(path)
    patched = path.read_text(encoding="utf-8")

    assert "TailwindV4Plugin(" in patched
    assert "var(--background)" in patched
    ast.parse(patched)


def test_strips_stale_bare_tailwind_plugin_entry(tmp_path: Path) -> None:
    path = _write_config(
        tmp_path,
        "import reflex as rx\n\n"
        'config = rx.Config(app_name="t", plugins=[rx.plugins.TailwindV4Plugin()])\n',
    )
    patch_rxconfig(path)
    patched = path.read_text(encoding="utf-8")

    # the stale, unconfigured entry is removed in favor of the fully
    # configured TailwindV4Plugin(...) block this function injects.
    assert "rx.plugins.TailwindV4Plugin()" not in patched
    assert "TailwindV4Plugin(\n" in patched
    ast.parse(patched)


# ── fallback path: AST pass can't find a plain `Assign` to rx.Config(...) ──


def test_falls_back_to_string_replace_when_ast_pass_cannot_match(
    tmp_path: Path,
) -> None:
    # An annotated assignment is an `ast.AnnAssign`, not the `ast.Assign` that
    # `_inject_via_ast` walks for, so it returns None and patch_rxconfig must
    # fall through to `_append_plugins_fallback`'s naive string replace on
    # "rx.Config(".
    path = _write_config(
        tmp_path,
        'import reflex as rx\n\nconfig: rx.Config = rx.Config(app_name="t")\n',
    )
    patch_rxconfig(path)
    patched = path.read_text(encoding="utf-8")

    assert "plugins=[" in patched
    assert "TailwindV4Plugin(" in patched
    assert "var(--background)" in patched


# ── warning paths: content left untouched, warning printed ─────────────────


def test_warns_and_leaves_file_untouched_when_no_rx_config_call_present(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    original = "x = 1\n"
    path = _write_config(tmp_path, original)

    patch_rxconfig(path)

    assert path.read_text(encoding="utf-8") == original
    assert "Could not automatically update rxconfig.py" in capsys.readouterr().out


def test_warns_and_leaves_file_untouched_when_config_is_unparseable(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    original = "def broken(:\n"
    path = _write_config(tmp_path, original)

    patch_rxconfig(path)

    assert path.read_text(encoding="utf-8") == original
    assert "Could not parse rxconfig.py" in capsys.readouterr().out


# ── command-level guard: a missing rxconfig.py is caught before patch_rxconfig ──


def test_cmd_init_exits_without_rxconfig_py(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # A missing config file is not an early return inside patch_rxconfig
    # itself (config_path.read_text() would raise before its try block) --
    # cmd_init guards against it before patch_rxconfig is ever called.
    monkeypatch.chdir(tmp_path)

    with pytest.raises(SystemExit) as exc_info:
        cmd_init()

    assert exc_info.value.code == 1
    assert "rxconfig.py not found" in capsys.readouterr().out
    assert not (tmp_path / "assets").exists()
