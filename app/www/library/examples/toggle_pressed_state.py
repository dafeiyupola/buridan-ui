import reflex as rx

from components.icons.hugeicon import hi
from components.ui.toggle import toggle


def toggle_pressed_state() -> rx.Component:
    return toggle(hi("TextItalicIcon", class_name="size-4"), default_pressed=True)
