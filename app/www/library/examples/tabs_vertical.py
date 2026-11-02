import reflex as rx

from components.ui.tabs import tabs


def tabs_vertical() -> rx.Component:
    return rx.el.div(
        tabs.root(
            tabs.list(
                tabs.indicator(),
                tabs.tab("Account", value="account"),
                tabs.tab("Password", value="password"),
                tabs.tab("Notifications", value="notifications"),
            ),
            default_value="account",
            orientation="vertical",
        ),
        class_name="flex justify-center text-sm",
    )
