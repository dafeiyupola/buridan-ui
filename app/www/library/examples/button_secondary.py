import reflex as rx

from components.ui.button import button


def button_secondary() -> rx.Component:
    return button("Secondary", variant="secondary")
