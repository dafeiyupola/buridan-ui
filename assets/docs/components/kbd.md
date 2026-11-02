

# Kbd

Used to display textual user input from keyboard.

## Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add kbd
```

### Manual Installation

```python
from typing import Any, Self

from reflex.components.component import ComponentNamespace
from reflex_components_core.el import (
    Div,
    Kbd as ElKbd,
)

from .core import CoreComponent


class ClassNames:
    KBD = (
        "pointer-events-none inline-flex h-5 w-fit min-w-5 items-center justify-center gap-1 "
        "rounded-sm bg-muted px-1 font-sans text-xs font-medium text-muted-foreground select-none "
        "in-data-[slot=tooltip-popup]:bg-background/20 in-data-[slot=tooltip-popup]:text-background "
        "dark:in-data-[slot=tooltip-popup]:bg-background/10 [&_svg:not([class*='size-'])]:size-3"
    )

    GROUP = "inline-flex items-center gap-1"


class KbdRoot(CoreComponent, ElKbd):
    @classmethod
    def create(cls, *children: Any, **props: Any) -> Self:
        props["data-slot"] = "kbd"

        cls.set_class_name(ClassNames.KBD, props)
        return super().create(*children, **props)


class KbdGroupContainer(CoreComponent, Div):
    @classmethod
    def create(cls, *children: Any, **props: Any) -> Self:
        props["data-slot"] = "kbd-group"

        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class KbdNamespace(ComponentNamespace):
    root = staticmethod(KbdRoot.create)
    group = staticmethod(KbdGroupContainer.create)
    class_names = ClassNames


kbd = KbdNamespace()
```


## Usage


```python
from components.ui.kbd import kbd
```


## Anatomy 
Use the following composition to build a `Kbd` component.


```python
kbd.group(
    kbd.root(),
    kbd.root(),
)
```


## Examples

## Group

Use the `kbd.group` component to group keyboard keys together.


```python
def kbd_as_group() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "Use ",
            kbd.group(
                kbd.root("Ctrl + B"),
                kbd.root("Ctrl + K"),
            ),
            " to open the command palette",
            class_name="text-sm text-muted-foreground",
        ),
        class_name="flex flex-col items-center gap-4",
    )
```


## Button

Use the `kbd.root` component inside a `Button` component to display a keyboard key inside a button.


```python
def kbd_button() -> rx.Component:
    return button(
        "Accept ",
        kbd.root(
            "⏎",
            data_icon="inline-end",
            class_name="translate-x-0.5",
        ),
        variant="outline",
    )
```


## Tooltip

You can use the `kbd.root` component inside a `Tooltip` component to display a tooltip with a keyboard key.


```python
def kbd_tooltip() -> rx.Component:
    return rx.el.div(
        button_group.root(
            tooltip.provider(
                tooltip.root(
                    tooltip.trigger(
                        render_=button("Save", variant="outline"),
                    ),
                    tooltip.portal(
                        tooltip.positioner(
                            tooltip.popup(
                                tooltip.arrow(),
                                "Save Changes ",
                                kbd.root("S"),
                            ),
                        ),
                    ),
                ),
                delay=0,
            ),
            tooltip.provider(
                tooltip.root(
                    tooltip.trigger(
                        render_=button("Print", variant="outline"),
                    ),
                    tooltip.portal(
                        tooltip.positioner(
                            tooltip.popup(
                                tooltip.arrow(),
                                "Print Document ",
                                kbd.group(
                                    kbd.root("Ctrl"),
                                    kbd.root("P"),
                                ),
                            ),
                        ),
                    ),
                ),
                delay=0,
            ),
        ),
        class_name="flex flex-wrap gap-4",
    )
```


## Input Group

You can use the `kbd.root` component inside a `input_group.addon` component to display a keyboard key inside an input group.


```python
def kbd_input_group() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Search..."),
            input_group.addon(
                hi("Search01Icon"),
                align="inline-start",
            ),
            input_group.addon(
                kbd.root("⌘"),
                kbd.root("K"),
                align="inline-end",
            ),
        ),
        class_name="flex w-full max-w-xs flex-col gap-6",
    )
```


## API Reference

## kbd.root

Use the `kbd.root` component to display a keyboard key.

| Prop         | Type     | Default |
| ------------ | -------- | ------- |
| `class_name` | `string` | ``      |

```python
kbd.root('Ctrl')
```

## kbd.group

Use the `kbd.group` component to group `kbd.root` components together.

| Prop         | Type     | Default |
| ------------ | -------- | ------- |
| `class_name` | `string` | ``      |

```python
kbd.group(
    kbd.root('Ctrl')
    kbd.root('B')
)
```
