import reflex as rx

from components.icons.hugeicon import hi
from components.ui.toggle import toggle


def toggle_disabled() -> rx.Component:
    return toggle(hi("TextUnderlineIcon", class_name="size-4"), disabled=True)
