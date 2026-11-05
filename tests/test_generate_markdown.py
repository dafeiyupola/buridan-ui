import ast
import inspect
import re

import pytest

from scripts.generate_markdown import (
    DOCS_SOURCE_DIR,
    DYNAMIC_LOAD_DIRS,
    align_markdown_tables,
    dynamic_load_components,
)

_DEMO_DELIMITER_RE = re.compile(r"--DEMO\(([\w_]+)\)--")


def _demo_names_referenced_in_docs() -> list[str]:
    """Every component name rendered via a ``--DEMO(name)--`` delimiter.

    These are the only snippets extracted with ``inspect.getsource`` on just
    the function itself (see ``_demo_block``), so they're the ones at risk of
    silently referencing a sibling helper that isn't shown in the docs.
    """
    names: set[str] = set()
    for md_file in DOCS_SOURCE_DIR.rglob("*.md"):
        names.update(_DEMO_DELIMITER_RE.findall(md_file.read_text(encoding="utf-8")))
    return sorted(names)


def _defined_function_names(tree: ast.AST) -> set[str]:
    return {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def _bare_name_foreach_callbacks(tree: ast.AST) -> set[str]:
    """Names passed as a plain identifier (not a lambda) for the ``render_fn``
    (second positional argument) of an ``rx.foreach(iterable, render_fn)`` call.
    """
    names: set[str] = set()
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "foreach"
            and len(node.args) >= 2
            and isinstance(node.args[1], ast.Name)
        ):
            names.add(node.args[1].id)
    return names


@pytest.mark.parametrize("demo_name", _demo_names_referenced_in_docs())
def test_demo_block_source_is_self_contained(demo_name: str) -> None:
    """A ``--DEMO(name)--`` snippet only ever shows ``name``'s own source.

    If ``name`` passes a named function (rather than an inline lambda) as a
    ``rx.foreach`` render callback, that function must be defined inside
    ``name`` itself -- a sibling, module-level helper would compile in the
    real app but silently vanish from the copy-pasted doc snippet.
    """
    registry = dynamic_load_components(DYNAMIC_LOAD_DIRS)
    obj, _ = registry[demo_name.lower()]
    source = inspect.getsource(obj)
    tree = ast.parse(source)

    defined = _defined_function_names(tree)
    referenced = _bare_name_foreach_callbacks(tree)

    assert referenced <= defined, (
        f"{demo_name} passes rx.foreach a named callback "
        f"({referenced - defined}) that isn't defined inside {demo_name} "
        f"itself, so it won't appear in the generated doc snippet"
    )


def test_align_table_emits_exactly_one_separator() -> None:
    table = "| Prop | Type |\n| --- | --- |\n| `size` | `str` |"

    assert align_markdown_tables(table) == (
        "| Prop   | Type  |\n| ------ | ----- |\n| `size` | `str` |"
    )


def test_align_table_keeps_escaped_pipes_inside_cells() -> None:
    table = '| Prop | Type |\n| --- | --- |\n| `size` | `"sm" \\| "xs"` |'

    assert align_markdown_tables(table) == (
        "| Prop   | Type           |\n"
        "| ------ | -------------- |\n"
        '| `size` | `"sm" \\| "xs"` |'
    )


def test_align_table_preserves_column_alignment_markers() -> None:
    table = "| Left | Center | Right |\n| :--- | :---: | ---: |\n| a | b | c |"

    assert align_markdown_tables(table) == (
        "| Left | Center | Right |\n| :--- | :----: | ----: |\n| a    | b      | c     |"
    )


def test_align_table_stops_at_first_line_not_starting_with_pipe() -> None:
    table = "| A | B |\n| --- | --- |\n| a | b |\nUse a | b to pipe."

    assert align_markdown_tables(table) == (
        "| A   | B   |\n| --- | --- |\n| a   | b   |\nUse a | b to pipe."
    )


def test_align_table_keeps_last_cell_of_row_without_trailing_pipe() -> None:
    table = "| A | B |\n| --- | --- |\n| a | b"

    assert align_markdown_tables(table) == (
        "| A   | B   |\n| --- | --- |\n| a   | b   |"
    )
