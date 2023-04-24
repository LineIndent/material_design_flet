import flet as ft
from flet_material.base import Theme


class FilterChip(ft.Container, Theme):
    def __init__(
        self,
        title: str,
        chip_width: int,
        *args,
        **kwargs,
    ):
        #
        self.title = title
        self.chip_width = chip_width

        #
        self.tick = ft.Control = ft.Checkbox(
            width=2,
            height=2,
            scale=ft.Scale(0.7),
            fill_color="#2e2f3e",
            check_color="white",
            disabled=True,
            value=False,
        )

        kwargs.setdefault("width", self.chip_width)
        kwargs.setdefault("bgcolor", "#2e2f3e")
        kwargs.setdefault("border", ft.border.all(1, Theme.primary_theme))
        kwargs.setdefault("padding", 8)
        kwargs.setdefault("ink", True)
        kwargs.setdefault("border_radius", 6)
        kwargs.setdefault("alignment", ft.alignment.center)
        kwargs.setdefault("on_click", lambda e: self.toggle_filter_chip(e))
        kwargs.setdefault(
            "content",
            ft.Row(
                spacing=0,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                vertical_alignment="center",
                controls=[self.tick, ft.Text(self.title, size=11, weight="bold")],
            ),
        )

        super().__init__(*args, **kwargs)

    def toggle_filter_chip(self, e):
        if self.tick.value == False:
            self.tick.value = True
        else:
            self.tick.value = False

        self.tick.update()
