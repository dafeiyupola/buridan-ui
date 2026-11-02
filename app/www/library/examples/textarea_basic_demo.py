import reflex as rx

from components.ui.textarea import textarea


def textarea_basic_demo() -> rx.Component:
    return textarea(placeholder="Type your message here.", class_name="max-w-xs")
