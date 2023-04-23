import flet as ft
from flet_material.base import Theme
import time


class CheckBox(ft.Container, Theme):
    def __init__(self, shape: str, *args, **kwargs):
        self.checkbox: ft.Control = ft.Checkbox(
            fill_color=Theme.primary_theme,
            check_color="white",
            scale=ft.Scale(0.95),
            on_change=lambda e: self.animate_checkbox(e),
        )

        kwargs.setdefault("width", 25)
        kwargs.setdefault("height", 25)
        kwargs.setdefault("shape", ft.BoxShape(shape))
        kwargs.setdefault("bgcolor", Theme.primary_theme)
        kwargs.setdefault("content", self.checkbox)
        kwargs.setdefault("scale", 0.9)
        kwargs.setdefault("animate_scale", ft.Animation(500, "bounceOut"))
        kwargs.setdefault("on_click", lambda e: self.animate_checkbox(e))

        super().__init__(*args, **kwargs)

    def animate_checkbox(self, e):
        self.scale = ft.Scale(0.85)
        self.update()
        time.sleep(0.15)
        self.scale = ft.Scale(1)
        self.update()
