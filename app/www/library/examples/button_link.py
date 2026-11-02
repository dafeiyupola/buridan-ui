import reflex as rx

from components.ui.button import button


def button_link() -> rx.Component:
    return button("Link", variant="link")
