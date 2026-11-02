

# Context Menu

Displays a menu of actions triggered by a right click.

## Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add context_menu
```

### Manual Installation

```python
from typing import Literal, Self

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.el import Span

from components.icons.hugeicon import hi

from .core import PACKAGE_NAME, BaseUIComponent, CoreComponent

LiteralMenuOrientation = Literal["vertical", "horizontal"]
LiteralSide = Literal["top", "right", "bottom", "left"]
LiteralAlign = Literal["start", "center", "end"]
LiteralPositionMethod = Literal["absolute", "fixed"]


class ClassNames:
    TRIGGER = "select-none"
    PORTAL = ""
    POPUP = "z-50 max-h-(--available-height) min-w-36 origin-(--transform-origin) overflow-x-hidden overflow-y-auto rounded-lg bg-popover p-1 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 outline-none data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95"
    ITEM = "group/context-menu-item relative flex cursor-default items-center gap-1.5 rounded-md px-1.5 py-1 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-7 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 focus:*:[svg]:text-accent-foreground data-[variant=destructive]:*:[svg]:text-destructive"
    SEPARATOR = "-mx-1 my-1 h-px bg-border"
    POSITIONER = "isolate z-50 outline-none"
    GROUP = ""
    GROUP_LABEL = (
        "px-1.5 py-1 text-xs font-medium text-muted-foreground data-inset:pl-7"
    )
    RADIO_GROUP = ""
    RADIO_ITEM = "relative flex cursor-default items-center gap-1.5 rounded-md py-1 pr-8 pl-1.5 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-7 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    RADIO_ITEM_INDICATOR = (
        "pointer-events-none absolute right-2 flex size-3.5 items-center justify-center"
    )
    CHECKBOX_ITEM = "relative flex cursor-default items-center gap-1.5 rounded-md py-1 pr-8 pl-1.5 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-7 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    CHECKBOX_ITEM_INDICATOR = (
        "pointer-events-none absolute right-2 flex size-3.5 items-center justify-center"
    )
    SUBMENU_TRIGGER = "flex cursor-default items-center gap-1.5 rounded-md px-1.5 py-1 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-7 data-open:bg-accent data-open:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    SHORTCUT = "ml-auto text-xs tracking-widest text-muted-foreground group-focus/context-menu-item:text-accent-foreground"


class ContextMenuBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/context-menu"

    @property
    def import_var(self) -> ImportVar:
        return ImportVar(tag="ContextMenu", package_path="", install=False)


class ContextMenuRoot(ContextMenuBaseComponent):
    tag = "ContextMenu.Root"

    default_open: Var[bool]
    open: Var[bool]
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]
    actions_ref: Var[str]
    close_parent_on_esc: Var[bool]
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]
    disabled: Var[bool]
    loop_focus: Var[bool]
    orientation: Var[LiteralMenuOrientation]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu"
        return super().create(*children, **props)


class ContextMenuTrigger(ContextMenuBaseComponent):
    tag = "ContextMenu.Trigger"

    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class ContextMenuPortal(ContextMenuBaseComponent):
    tag = "ContextMenu.Portal"

    container: Var[str]
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-portal"
        cls.set_class_name(ClassNames.PORTAL, props)
        return super().create(*children, **props)


class ContextMenuPositioner(ContextMenuBaseComponent):
    tag = "ContextMenu.Positioner"

    collision_avoidance: Var[str | dict[str, str]]
    align: Var[LiteralAlign]
    align_offset: Var[int]
    side: Var[LiteralSide]
    side_offset: Var[int]
    arrow_padding: Var[int]
    collision_padding: Var[int]
    collision_boundary: Var[str]
    sticky: Var[bool]
    disable_anchor_tracking: Var[bool]
    position_method: Var[LiteralPositionMethod]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-positioner"
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class ContextMenuPopup(ContextMenuBaseComponent):
    tag = "ContextMenu.Popup"

    final_focus: Var[str]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-content"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class ContextMenuItem(ContextMenuBaseComponent):
    tag = "ContextMenu.Item"

    label: Var[str]
    close_on_click: Var[bool]
    native_button: Var[bool]
    disabled: Var[bool]
    inset: Var[bool]
    variant: Var[str]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-item"
        if props.get("inset"):
            props["data-inset"] = props.pop("inset")
        if props.get("variant"):
            props["data-variant"] = props.pop("variant")
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class ContextMenuSeparator(ContextMenuBaseComponent):
    tag = "ContextMenu.Separator"

    orientation: Var[LiteralMenuOrientation]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-separator"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class ContextMenuGroup(ContextMenuBaseComponent):
    tag = "ContextMenu.Group"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-group"
        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class ContextMenuGroupLabel(ContextMenuBaseComponent):
    tag = "ContextMenu.GroupLabel"

    inset: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-label"
        if props.get("inset"):
            props["data-inset"] = props.pop("inset")
        cls.set_class_name(ClassNames.GROUP_LABEL, props)
        return super().create(*children, **props)


class ContextMenuRadioGroup(ContextMenuBaseComponent):
    tag = "ContextMenu.RadioGroup"

    default_value: Var[str | int]
    value: Var[str | int]
    on_value_change: EventHandler[passthrough_event_spec(str | int, dict)]
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-radio-group"
        cls.set_class_name(ClassNames.RADIO_GROUP, props)
        return super().create(*children, **props)


class ContextMenuRadioItem(ContextMenuBaseComponent):
    tag = "ContextMenu.RadioItem"

    label: Var[str]
    value: Var[str | int]
    close_on_click: Var[bool]
    native_button: Var[bool]
    disabled: Var[bool]
    inset: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-radio-item"
        if props.get("inset"):
            props["data-inset"] = props.pop("inset")
        cls.set_class_name(ClassNames.RADIO_ITEM, props)
        return super().create(*children, **props)


class ContextMenuRadioItemIndicator(ContextMenuBaseComponent):
    tag = "ContextMenu.RadioItemIndicator"

    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-radio-item-indicator"
        cls.set_class_name(ClassNames.RADIO_ITEM_INDICATOR, props)
        return super().create(*children, **props)


class ContextMenuCheckboxItem(ContextMenuBaseComponent):
    tag = "ContextMenu.CheckboxItem"

    label: Var[str]
    default_checked: Var[bool]
    checked: Var[bool]
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]
    close_on_click: Var[bool]
    native_button: Var[bool]
    disabled: Var[bool]
    inset: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-checkbox-item"
        if props.get("inset"):
            props["data-inset"] = props.pop("inset")
        cls.set_class_name(ClassNames.CHECKBOX_ITEM, props)
        return super().create(*children, **props)


class ContextMenuCheckboxItemIndicator(ContextMenuBaseComponent):
    tag = "ContextMenu.CheckboxItemIndicator"

    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-checkbox-item-indicator"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM_INDICATOR, props)
        return super().create(*children, **props)


class ContextMenuSubmenuRoot(ContextMenuBaseComponent):
    tag = "ContextMenu.SubmenuRoot"

    default_open: Var[bool]
    open: Var[bool]
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]
    close_parent_on_esc: Var[bool]
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]
    disabled: Var[bool]
    loop_focus: Var[bool]
    orientation: Var[LiteralMenuOrientation]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-sub"
        return super().create(*children, **props)


class ContextMenuSubmenuTrigger(ContextMenuBaseComponent):
    tag = "ContextMenu.SubmenuTrigger"

    label: Var[str]
    native_button: Var[bool]
    open_on_hover: Var[bool]
    delay: Var[int]
    close_delay: Var[int]
    inset: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-sub-trigger"
        if props.get("inset"):
            props["data-inset"] = props.pop("inset")
        cls.set_class_name(ClassNames.SUBMENU_TRIGGER, props)
        return super().create(
            *children,
            hi("ArrowRight01Icon", class_name="ml-auto"),
            **props,
        )


class ContextMenuShortcut(CoreComponent, Span):
    @classmethod
    def create(cls, *children, **props) -> Self:
        props["data-slot"] = "context-menu-shortcut"
        cls.set_class_name(ClassNames.SHORTCUT, props)
        return super().create(*children, **props)


class ContextMenu(ComponentNamespace):
    root = staticmethod(ContextMenuRoot.create)
    trigger = staticmethod(ContextMenuTrigger.create)
    portal = staticmethod(ContextMenuPortal.create)
    positioner = staticmethod(ContextMenuPositioner.create)
    popup = staticmethod(ContextMenuPopup.create)
    item = staticmethod(ContextMenuItem.create)
    separator = staticmethod(ContextMenuSeparator.create)
    group = staticmethod(ContextMenuGroup.create)
    group_label = staticmethod(ContextMenuGroupLabel.create)
    radio_group = staticmethod(ContextMenuRadioGroup.create)
    radio_item = staticmethod(ContextMenuRadioItem.create)
    radio_item_indicator = staticmethod(ContextMenuRadioItemIndicator.create)
    checkbox_item = staticmethod(ContextMenuCheckboxItem.create)
    checkbox_item_indicator = staticmethod(ContextMenuCheckboxItemIndicator.create)
    sub = staticmethod(ContextMenuSubmenuRoot.create)
    sub_trigger = staticmethod(ContextMenuSubmenuTrigger.create)
    shortcut = staticmethod(ContextMenuShortcut.create)
    class_names = ClassNames


context_menu = ContextMenu()
```


## Usage


```python
from components.ui.context_menu import context_menu
```


## Anatomy 

Use the following composition to build a `Context Menu` component.


```python
context_menu.root(
    context_menu.trigger(),
    context_menu.portal(
        context_menu.positioner(
            context_menu.popup(
                context_menu.item(),
                context_menu.separator(),
                context_menu.group(
                    context_menu.group_label(),
                    context_menu.item(),
                ),
                context_menu.checkbox_item(
                    context_menu.checkbox_item_indicator(),
                ),
                context_menu.radio_group(
                    context_menu.radio_item(
                        context_menu.radio_item_indicator(),
                    ),
                ),
                context_menu.sub(
                    context_menu.sub_trigger(),
                    context_menu.portal(
                        context_menu.positioner(
                            context_menu.popup(),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
```


A Context Menu is built by composing a root trigger with an overlay surface.

```composition
context_menu.root
├── context_menu.trigger
└── context_menu.portal
    └── context_menu.positioner
        └── context_menu.popup
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   ├── context_menu.item
            │   └── context_menu.item
            ├── context_menu.separator
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   ├── context_menu.checkbox_item
            │   │   └── context_menu.checkbox_item_indicator
            │   └── context_menu.checkbox_item
            │       └── context_menu.checkbox_item_indicator
            ├── context_menu.separator
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   └── context_menu.radio_group
            │       ├── context_menu.radio_item
            │       │   └── context_menu.radio_item_indicator
            │       └── context_menu.radio_item
            │           └── context_menu.radio_item_indicator
            └── context_menu.sub
                ├── context_menu.sub_trigger
                └── context_menu.portal
                    └── context_menu.positioner
                        └── context_menu.popup
                            └── context_menu.group
                                ├── context_menu.item
                                └── context_menu.item
```

## Examples

## Basic

A simple context menu with a few actions.


```python
def context_menu_basic() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-input border-dashed text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.item("Back"),
                        context_menu.item("Forward", disabled=True),
                        context_menu.item("Reload"),
                    ),
                ),
            ),
        ),
    )
```


## Submenu

Use `context_menu.sub` to nest secondary actions.


```python
def context_menu_submenu() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.item(
                            "Copy",
                            context_menu.shortcut("⌘C"),
                        ),
                        context_menu.item(
                            "Cut",
                            context_menu.shortcut("⌘X"),
                        ),
                    ),
                    context_menu.sub(
                        context_menu.sub_trigger("More Tools"),
                        context_menu.portal(
                            context_menu.positioner(
                                context_menu.popup(
                                    context_menu.group(
                                        context_menu.item("Save Page..."),
                                        context_menu.item("Create Shortcut..."),
                                        context_menu.item("Name Window..."),
                                    ),
                                    context_menu.separator(),
                                    context_menu.group(
                                        context_menu.item("Developer Tools"),
                                    ),
                                    context_menu.separator(),
                                    context_menu.group(
                                        context_menu.item(
                                            "Delete",
                                            variant="destructive",
                                        ),
                                    ),
                                    class_name="shadow-lg",
                                ),
                                side="right",
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Shortcuts

Use `context_menu.shortcut` to show keyboard hints.


```python
def context_menu_shortcuts() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.item(
                            "Back",
                            context_menu.shortcut("⌘["),
                        ),
                        context_menu.item(
                            "Forward",
                            context_menu.shortcut("⌘]"),
                            disabled=True,
                        ),
                        context_menu.item(
                            "Reload",
                            context_menu.shortcut("⌘R"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Save",
                            context_menu.shortcut("⌘S"),
                        ),
                        context_menu.item(
                            "Save As...",
                            context_menu.shortcut("⇧⌘S"),
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Groups

Group related actions and separate them with dividers.


```python
def context_menu_groups() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.group_label("File"),
                        context_menu.item(
                            "New File",
                            context_menu.shortcut("⌘N"),
                        ),
                        context_menu.item(
                            "Open File",
                            context_menu.shortcut("⌘O"),
                        ),
                        context_menu.item(
                            "Save",
                            context_menu.shortcut("⌘S"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.group_label("Edit"),
                        context_menu.item(
                            "Undo",
                            context_menu.shortcut("⌘Z"),
                        ),
                        context_menu.item(
                            "Redo",
                            context_menu.shortcut("⇧⌘Z"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Cut",
                            context_menu.shortcut("⌘X"),
                        ),
                        context_menu.item(
                            "Copy",
                            context_menu.shortcut("⌘C"),
                        ),
                        context_menu.item(
                            "Paste",
                            context_menu.shortcut("⌘V"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Delete",
                            context_menu.shortcut("⌫"),
                            variant="destructive",
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Checkboxes

Use `context_menu.checkbox_item` for toggles.


```python
def context_menu_checkboxes() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4"),
                            ),
                            "Show Bookmarks Bar",
                            default_checked=True,
                        ),
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4"),
                            ),
                            "Show Full URLs",
                        ),
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4"),
                            ),
                            "Show Developer Tools",
                            default_checked=True,
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Radio

Use `context_menu.radio_item` for exclusive choices.


```python
def context_menu_radio() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.group_label("People"),
                        context_menu.radio_group(
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4"),
                                ),
                                "Pedro Duarte",
                                value="pedro",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4"),
                                ),
                                "Colm Tuite",
                                value="colm",
                            ),
                            value=selected_user.value,
                            on_value_change=selected_user.set_value,
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.group_label("Theme"),
                        context_menu.radio_group(
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4"),
                                ),
                                "Light",
                                value="light",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4"),
                                ),
                                "Dark",
                                value="dark",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4"),
                                ),
                                "System",
                                value="system",
                            ),
                            value=selected_theme.value,
                            on_value_change=selected_theme.set_value,
                        ),
                    ),
                ),
            ),
        ),
    )
```



## Sides

Control submenu placement with side and align props.


```python
def context_menu_sides() -> rx.Component:
    return rx.el.div(
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (top)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (top)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="top",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (right)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (right)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="right",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (bottom)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (bottom)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="bottom",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (left)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (left)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="left",
                ),
            ),
        ),
        class_name="grid w-full max-w-sm grid-cols-2 gap-4",
    )
```

