"""Tests for the `input_group` namespace's `unstyled` contract (issue #167).

`InputGroupInput`, `InputGroupTextarea`, and `InputGroupButton` used to
pre-bake their default classes into `props["class_name"]` via `cn()` before
delegating to `input()`/`textarea()`/`button()`, bypassing
`CoreComponent.set_class_name` entirely. `unstyled=True` therefore never
dropped the group-control defaults, unlike `input_group.root`/`addon`/`text`,
which already routed through `set_class_name`.

These tests pin the fix: the control wrappers merge their own defaults via
`set_class_name` and forward `unstyled` to the inner component so its
defaults are dropped too.
"""

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from components.ui.input import ClassNames as InputClassNames  # noqa: E402
from components.ui.input_group import ClassNames, input_group  # noqa: E402
from components.ui.textarea import ClassNames as TextAreaClassNames  # noqa: E402

# ---------------------------------------------------------------------------
# input_group.input
# ---------------------------------------------------------------------------


def test_input_group_input_unstyled_strips_all_defaults() -> None:
    comp = input_group.input(class_name="custom-input", unstyled=True)

    assert str(comp.class_name) == "custom-input"


def test_input_group_input_unstyled_does_not_leak_onto_dom() -> None:
    comp = input_group.input(class_name="custom-input", unstyled=True)
    rendered = json.dumps(comp.render())

    assert "unstyled" not in rendered


def test_input_group_input_default_merges_control_and_input_classes() -> None:
    comp = input_group.input(class_name="custom-input")
    class_name = str(comp.class_name)

    assert ClassNames.CONTROL_INPUT in class_name
    assert InputClassNames.INPUT in class_name
    assert "custom-input" in class_name


def test_input_group_input_preserves_type_and_data_slot() -> None:
    comp = input_group.input()

    rendered_props = " ".join(comp.render()["props"])
    assert 'type:"text"' in rendered_props
    assert '"data-slot":"input-group-control"' in rendered_props


# ---------------------------------------------------------------------------
# input_group.textarea
# ---------------------------------------------------------------------------


def test_input_group_textarea_unstyled_strips_all_defaults() -> None:
    comp = input_group.textarea(class_name="custom-textarea", unstyled=True)

    assert str(comp.class_name) == "custom-textarea"


def test_input_group_textarea_unstyled_does_not_leak_onto_dom() -> None:
    comp = input_group.textarea(class_name="custom-textarea", unstyled=True)
    rendered = json.dumps(comp.render())

    assert "unstyled" not in rendered


def test_input_group_textarea_default_merges_control_and_textarea_classes() -> None:
    comp = input_group.textarea(class_name="custom-textarea")
    class_name = str(comp.class_name)

    assert ClassNames.CONTROL_TEXTAREA in class_name
    assert TextAreaClassNames.ROOT in class_name
    assert "custom-textarea" in class_name


def test_input_group_textarea_preserves_data_slot() -> None:
    comp = input_group.textarea()

    rendered_props = " ".join(comp.render()["props"])
    assert '"data-slot":"input-group-control"' in rendered_props


# ---------------------------------------------------------------------------
# input_group.button
# ---------------------------------------------------------------------------


def test_input_group_button_unstyled_drops_wrapper_defaults() -> None:
    comp = input_group.button("x", class_name="custom-button", unstyled=True)
    class_name = str(comp.class_name)

    assert "flex items-center gap-2 text-sm shadow-none" not in class_name
    assert ClassNames.get_button_size("xs") not in class_name


def test_input_group_button_default_merges_wrapper_and_size_classes() -> None:
    comp = input_group.button("x", class_name="custom-button")
    class_name = str(comp.class_name)

    assert "flex items-center gap-2 text-sm shadow-none" in class_name
    assert ClassNames.get_button_size("xs") in class_name
    assert "custom-button" in class_name


def test_input_group_button_preserves_type_and_data_size() -> None:
    comp = input_group.button("x")

    rendered_props = " ".join(comp.render()["props"])
    assert 'type:"button"' in rendered_props
    assert '"data-size":"xs"' in rendered_props


def test_input_group_button_honors_explicit_size() -> None:
    comp = input_group.button("x", size="icon-sm")
    class_name = str(comp.class_name)

    assert ClassNames.get_button_size("icon-sm") in class_name

    rendered_props = " ".join(comp.render()["props"])
    assert '"data-size":"icon-sm"' in rendered_props
