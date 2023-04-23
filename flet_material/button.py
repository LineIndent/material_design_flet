import flet as ft
from flet_material.base import Theme


class Buttons(ft.Container, Theme):
    def __init__(self, width, height, title: str, *args, **kwargs):
        #
        self.title = title
        #
        self.text = ft.Text(
            self.title,
            weight="bold",
            color=ft.colors.with_opacity(0.85, Theme.primary_theme),
        )
        #
        kwargs.setdefault("width", width)
        kwargs.setdefault("height", height)
        kwargs.setdefault("ink", True)
        kwargs.setdefault("bgcolor", "#2e2f3e")
        kwargs.setdefault("shape", ft.BoxShape("rectangle"))
        kwargs.setdefault(
            "border",
            ft.border.all(2, ft.colors.with_opacity(0.85, Theme.primary_theme)),
        )
        kwargs.setdefault("border_radius", 4)
        kwargs.setdefault("on_hover", lambda e: self.animate_button(e))
        kwargs.setdefault("alignment", ft.alignment.center)
        kwargs.setdefault("animate", ft.Animation(500, "ease"))
        kwargs.setdefault("content", self.text)

        super().__init__(*args, **kwargs)

    def animate_button(self, e):
        if self.bgcolor == "#2e2f3e":
            self.bgcolor = Theme.primary_theme
            self.text.color = ft.colors.with_opacity(0.95, "white")
        else:
            self.bgcolor = "#2e2f3e"
            self.text.color = ft.colors.with_opacity(0.85, Theme.primary_theme)

        self.update()
