# noqa: INP001
"""Regression guard for the FBT001/FBT002 clean-up (issue #253 / #243).

Each of these boolean parameters was made keyword-only to clear ruff's
FBT001/FBT002 findings. These tests pin the resulting signature contract so a
future edit cannot quietly reintroduce a positional boolean trap: calling with
the boolean positionally must raise ``TypeError``, and calling with the
boolean by keyword must keep working.
"""

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app.templates.options import component_panel, menu_panel  # noqa: E402
from app.www.library.charts.chart_tooltip import (  # noqa: E402
    chart_tooltip as app_chart_tooltip,
)
from components.charts.chart_tooltip import chart_tooltip  # noqa: E402
from components.ui.table import high_level_table  # noqa: E402
from scripts import generate_search_index  # noqa: E402


def test_options_panel_rejects_positional_desktop_and_accepts_keyword() -> None:
    with pytest.raises(TypeError):
        component_panel(False)  # noqa: FBT003  # pyright: ignore[reportCallIssue]  # pyrefly: ignore[bad-argument-count]  # ty: ignore[too-many-positional-arguments]
    component_panel(desktop=False)
    menu_panel()


def test_chart_tooltip_rejects_positional_bool_and_accepts_keyword() -> None:
    with pytest.raises(TypeError):
        chart_tooltip("show", True)  # noqa: FBT003  # pyright: ignore[reportCallIssue]  # pyrefly: ignore[bad-argument-count]  # ty: ignore[too-many-positional-arguments]
    chart_tooltip("show", is_animation_active=True)
    app_chart_tooltip("hide")


def test_high_level_table_rejects_positional_striped_and_accepts_keyword() -> None:
    data = [{"a": "1"}]
    with pytest.raises(TypeError):
        high_level_table(data, None, True)  # noqa: FBT003  # pyright: ignore[reportCallIssue]  # pyrefly: ignore[bad-argument-count]  # ty: ignore[too-many-positional-arguments]
    high_level_table(data, striped=True)


def test_generate_search_index_rejects_positional_include_reflex() -> None:
    with pytest.raises(TypeError):
        generate_search_index.generate_search_index({}, True)  # noqa: FBT003  # pyright: ignore[reportCallIssue]  # pyrefly: ignore[bad-argument-count]  # ty: ignore[too-many-positional-arguments]
