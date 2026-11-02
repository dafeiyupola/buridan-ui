from typing import Any, cast

import reflex as rx
from reflex.experimental import ClientStateVar


# Used in --demo(form_state_pattern_example)--
def form_state_pattern_example():
    form_state = cast("Any", ClientStateVar.create("form", {}))

    def update_username(v: object) -> object:
        return form_state.set_value(form_state.value.merge({"username": v}))

    return rx.el.input(
        value=form_state.value.get("username", ""),
        on_change=cast("Any", update_username),
    )
