import reflex as rx

from components.ui.button import button


def button_destructive() -> rx.Component:
    return button("Destructive", variant="destructive")
