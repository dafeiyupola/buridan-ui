

# Button Group

A container that groups related buttons together with consistent styling.

## Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add button_group
```

### Manual Installation

```python
from typing import Literal, Self

from reflex.components.component import ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.core.cond import cond
from reflex_components_core.el import Div

from .core import CoreComponent, cn
from .separator import SeparatorComponent


class ClassNames:
    BASE_GROUP = "flex w-fit items-stretch *:focus-visible:relative *:focus-visible:z-10 has-[>[data-slot=button-group]]:gap-2 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-lg [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1"
    HORIZONTAL = "*:data-slot:rounded-r-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-r-lg! [&>[data-slot]~[data-slot]]:rounded-l-none [&>[data-slot]~[data-slot]]:border-l-0"
    VERTICAL = "flex-col *:data-slot:rounded-b-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-b-lg! [&>[data-slot]~[data-slot]]:rounded-t-none [&>[data-slot]~[data-slot]]:border-t-0"
    TEXT = "flex items-center gap-2 rounded-lg border bg-muted px-2.5 text-sm font-medium [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4"
    SEPARATOR = "relative self-stretch bg-input data-[orientation=horizontal]:mx-px data-[orientation=horizontal]:w-auto data-[orientation=vertical]:my-px data-[orientation=vertical]:h-auto"


class ButtonGroupRoot(CoreComponent, Div):
    orientation: Var[Literal["horizontal", "vertical"]]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "button-group"
        orientation = props.get("orientation", "horizontal")

        variant_class = cond(
            orientation == "horizontal",
            ClassNames.HORIZONTAL,
            ClassNames.VERTICAL,
        )
        combined_class = cn(ClassNames.BASE_GROUP, variant_class)

        cls.set_class_name(combined_class, props)

        props["role"] = "group"
        props["data-orientation"] = orientation

        return super().create(*children, **props)


class ButtonGroupText(CoreComponent, Div):
    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "button-group-text"
        cls.set_class_name(ClassNames.TEXT, props)
        return super().create(*children, **props)


class ButtonGroupSeparator(SeparatorComponent):
    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "button-group-separator"

        if "orientation" not in props:
            props["orientation"] = "vertical"

        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class ButtonGroup(ComponentNamespace):
    root = staticmethod(ButtonGroupRoot.create)
    text = staticmethod(ButtonGroupText.create)
    separator = staticmethod(ButtonGroupSeparator.create)


button_group = ButtonGroup()
```


## Usage


```python
from components.ui.button_group import button_group
```


## Anatomy 
Use the following composition to build a `Button Group` component.


```python
button_group.root(
    button(),
    button_group.separator(),
)
```



## Accessibility

- The `button_group.root` component has the `role` attribute set to `group`.
- Use `Tab` to navigate between the buttons in the group.
- Use `aria-label` or `aria-labelledby` to label the button group.

## Examples

## Orientation

Set the `orientation` prop to change the button group layout.


```python
def button_group_orientation() -> rx.Component:
    return button_group.root(
        button(
            hi("Add01Icon"),
            variant="outline",
            size="icon",
        ),
        button(
            hi("MinusSignIcon"),
            variant="outline",
            size="icon",
        ),
        orientation="vertical",
        aria_label="Media controls",
        class_name="h-fit",
    )
```


## Size

Control the size of buttons using the `size` prop on individual buttons.


```python
def button_group_size() -> rx.Component:
    return rx.el.div(
        button_group.root(
            button("Small", variant="outline", size="sm"),
            button("Button", variant="outline", size="sm"),
            button("Group", variant="outline", size="sm"),
            button(hi("Add01Icon"), variant="outline", size="icon-sm"),
        ),
        button_group.root(
            button("Default", variant="outline"),
            button("Button", variant="outline"),
            button("Group", variant="outline"),
            button(hi("Add01Icon"), variant="outline", size="icon"),
        ),
        button_group.root(
            button("Large", variant="outline", size="lg"),
            button("Button", variant="outline", size="lg"),
            button("Group", variant="outline", size="lg"),
            button(hi("Add01Icon"), variant="outline", size="icon-lg"),
        ),
        class_name="flex flex-col items-start gap-8",
    )
```


## Separator

The `button_group.separator` component visually divides buttons within a group.

Buttons with variant `outline` do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.


```python
def button_group_separator() -> rx.Component:
    return button_group.root(
        button("Copy", variant="secondary", size="sm"),
        button_group.separator(),
        button("Paste", variant="secondary", size="sm"),
    )
```


## Split

Create a split button group by adding two buttons separated by a `button_group.separator`.


```python
def button_group_split() -> rx.Component:
    return button_group.root(
        button("Button", variant="secondary"),
        button_group.separator(),
        button(
            hi("Add01Icon"),
            variant="secondary",
            size="icon",
        ),
    )
```


## Input

Wrap an `input` component with buttons.


```python
def button_group_input() -> rx.Component:
    return button_group.root(
        input(placeholder="Search..."),
        button(
            hi("Search01Icon"),
            variant="outline",
            aria_label="Search",
        ),
    )
```


## Dropdown Menu

Create a split button group with a `menu` component.


```python
def button_group_dropdown() -> rx.Component:
    return button_group.root(
        button("Follow", variant="outline"),
        menu.root(
            menu.trigger(
                render_=button(
                    hi("ArrowDown01Icon"),
                    variant="outline",
                    class_name="pl-2!",
                ),
            ),
            menu.portal(
                menu.positioner(
                    menu.popup(
                        menu.group(
                            menu.item("Mute Conversation"),
                            menu.item("Mark as Read"),
                            menu.item("Report Conversation"),
                            menu.item("Block User"),
                            menu.item("Share Conversation"),
                            menu.item("Copy Conversation"),
                        ),
                        menu.separator(),
                        menu.group(
                            menu.item("Delete Conversation", variant="destructive"),
                        ),
                        class_name="w-44",
                    ),
                    align="end",
                ),
            ),
        ),
    )
```



## Select

Pair with a `select` component.


```python
def button_group_select() -> rx.Component:

    return button_group.root(
        button_group.root(
            select.root(
                select.trigger(
                    selected_currency.value,
                    select.icon(),
                    class_name="flex items-center gap-1",
                ),
                select.portal(
                    select.positioner(
                        select.popup(
                            select.group(
                                *[
                                    select.item(
                                        select.item_text(
                                            item["value"],
                                            " ",
                                            rx.el.span(
                                                item["label"],
                                                class_name="text-xs !text-muted-foreground",
                                            ),
                                            class_name="text-sm text-foreground",
                                        ),
                                        select.item_indicator(),
                                        value=item["value"],
                                        class_name="flex flex-row items-center justify-between",
                                    )
                                    for item in currencies
                                ],
                            ),
                        ),
                        align="start",
                    ),
                ),
                items=currencies,
                value=selected_currency.value,
                on_value_change=selected_currency.set_value,
                name="currency_select",
            ),
            input(placeholder="10.00", pattern="[0-9]*"),
        ),
        button_group.root(
            button(
                hi("ArrowRight01Icon"),
                aria_label="Send",
                size="icon",
                variant="outline",
            ),
        ),
    )
```


## API Reference

## button_group.root

The `button_group.root` component is a container that groups related buttons together with consistent styling.

| Prop          | Type                         | Default        |
| ------------- | ---------------------------- | -------------- |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` |


## button_group.separator

The `button_group.separator` component visually divides buttons within a group.

| Prop          | Type                         | Default      |
| ------------- | ---------------------------- | ------------ |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` |


## button_group.text

Use this component to display text within a button group.

| Prop        | Type           | Default |
| ----------- | -------------- | ------- |
| `*children` | `rx.Component` | `false` |


The `button_group.text` accepts `*children` so any interactive component passed to it will be rendered. Use it to render a custom component as the text, for example a label.
