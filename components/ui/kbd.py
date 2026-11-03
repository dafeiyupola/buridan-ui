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
