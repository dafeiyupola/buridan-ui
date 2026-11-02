import reflex as rx

from components.ui.button import button


def button_outline() -> rx.Component:
    return button("Outline", variant="outline")
