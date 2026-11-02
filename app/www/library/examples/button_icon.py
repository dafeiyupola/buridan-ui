import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button


def button_icon() -> rx.Component:
    return button(
        hi("CircleArrowUp01Icon", class_name="size-4"),
        variant="outline",
        size="icon",
    )
