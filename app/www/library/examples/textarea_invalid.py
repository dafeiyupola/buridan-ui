import reflex as rx

from components.ui.field import field
from components.ui.textarea import textarea


def textarea_invalid() -> rx.Component:
    return field.root(
        field.label(
            "Message",
            html_for="textarea-invalid",
        ),
        textarea(
            id="textarea-invalid",
            placeholder="Type your message here.",
            **{"aria-invalid": True},
        ),
        field.description(
            "Please enter a valid message.",
        ),
        **{"data-invalid": True},
        class_name="max-w-xs",
    )
