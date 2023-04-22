import flet as ft
from flet_material.base import Theme


class Switchs(ft.Container, Theme):
    def __init__(self, animation: ft.Animation = "easeInOutBack", *args, **kwargs):
        self.toggle = ft.Container(
            bgcolor="white",
            shape=ft.BoxShape("circle"),
            offset=ft.transform.Offset(-0.25, 0),
            animate_offset=ft.Animation(600, animation),
            on_click=lambda e: self.toggle_switch(e),
        )

        kwargs.setdefault("width", 54)
        kwargs.setdefault("height", 25)
        kwargs.setdefault("border_radius", 25)
        kwargs.setdefault("bgcolor", "white10")
        kwargs.setdefault("padding", 4)
        kwargs.setdefault("clip_behavior", ft.ClipBehavior.HARD_EDGE)
        kwargs.setdefault("content", self.toggle)
        kwargs.setdefault("animate", 400)
        kwargs.setdefault("on_click", lambda e: self.toggle_switch(e))

        super().__init__(*args, **kwargs)

    def toggle_switch(self, e):
        if self.toggle.offset == ft.transform.Offset(-0.25, 0):
            self.toggle.offset = ft.transform.Offset(0.25, 0)
            self.bgcolor = Theme.primary_theme
            self.update()
        elif self.toggle.offset == ft.transform.Offset(0.25, 0):
            self.toggle.offset = ft.transform.Offset(-0.25, 0)
            self.bgcolor = "white10"
            self.update()
        else:
            pass
