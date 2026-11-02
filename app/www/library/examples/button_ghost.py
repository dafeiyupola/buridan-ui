import reflex as rx

from components.ui.button import button


def button_ghost() -> rx.Component:
    return button("Ghost", variant="ghost")
