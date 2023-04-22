import flet as ft
from styles import alert_dimension, alert_settings
from flet_material.base import Theme


class Alerts(ft.Container, Theme):
    def __init__(
        self,
        type_: str,
        size: str,
        title: str,
        comment: str,
        *args,
        **kwargs,
    ):
        # get alert dimensions
        width = alert_dimension.get(size).get("width")
        height = alert_dimension.get(size).get("height")

        # get alert properties
        bgcolor = alert_settings.get(type_).get("bgcolor")
        icon = alert_settings.get(type_).get("icon")

        # props for inner row
        self.box1: ft.Control = ft.Container(
            width=5,
            border_radius=20,
            bgcolor=bgcolor,
            margin=ft.margin.only(left=5, right=5, top=5, bottom=5),
        )
        self.box2: ft.Control = ft.Container(
            expand=1,
            alignment=ft.alignment.center,
            content=ft.Icon(name=icon, size=30, color=bgcolor),
        )
        self.box3: ft.Control = ft.Container(
            expand=5,
            content=ft.Row(
                alignment="start",
                controls=[
                    ft.Column(
                        spacing=2,
                        alignment="center",
                        controls=[
                            ft.Text(title, size=13, color="black", weight="bold"),
                            ft.Text(
                                comment,
                                size=10,
                                color=ft.colors.with_opacity(0.85, "black"),
                            ),
                        ],
                    )
                ],
            ),
        )
        self.box4: ft.Control = ft.Container(
            width=45,
            alignment=ft.alignment.center,
            ink=True,
            content=ft.Text("×", color=ft.colors.with_opacity(0.5, "black")),
        )

        #
        kwargs.setdefault(
            "shadow",
            ft.BoxShadow(
                spread_radius=8,
                blur_radius=15,
                color=ft.colors.with_opacity(0.25, "black"),
                offset=ft.Offset(4, 0),
            ),
        )
        kwargs.setdefault("width", width)
        kwargs.setdefault("height", height)
        kwargs.setdefault("bgcolor", ft.colors.with_opacity(0.90, "white"))
        kwargs.setdefault("border_radius", 6)
        kwargs.setdefault(
            "content",
            ft.Row(
                spacing=0,
                alignment="center",
                controls=[self.box1, self.box2, self.box3, self.box4],
            ),
        )

        super().__init__(*args, **kwargs)
