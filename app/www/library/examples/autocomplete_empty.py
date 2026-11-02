import reflex as rx

from components.ui.autocomplete import autocomplete


def autocomplete_empty_state() -> rx.Component:
    return autocomplete(
        items=["feature", "fix", "bug"],
        placeholder="Try typing something that won't match...",
        empty_class="text-destructive py-6",
    )
