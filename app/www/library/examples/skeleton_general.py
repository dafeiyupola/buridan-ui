import reflex as rx

from components.ui.skeleton import skeleton_component


def skeleton_general() -> rx.Component:
    return skeleton_component(class_name="h-8 w-32 rounded-md")
