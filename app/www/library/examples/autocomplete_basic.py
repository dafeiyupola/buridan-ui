import reflex as rx

from components.ui.autocomplete import autocomplete


def autocomplete_basic() -> rx.Component:
    return autocomplete(
        items=["feature", "fix", "bug", "docs", "internal", "mobile"],
        placeholder="Search tags...",
    )
