import flet as ft
from styles import admon_style, font_scheme


class Admonition(ft.Container):
    def __init__(
        self,
        type_: str,
        expanded_height: int,
        expand: bool,
        components: list,
        height=60,
        padding=0,
        border_radius=6,
        animate=ft.Animation(300, "decelerate"),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        shadow=ft.BoxShadow(
            spread_radius=8,
            blur_radius=15,
            color=ft.colors.with_opacity(0.35, "black"),
            offset=ft.Offset(4, 4),
        ),
    ):
        self.type_ = type_
        self.expanded_height = expanded_height
        self.components = components
        self.column = ft.Column(
            controls=self.components,
        )

        # define admonition title properties
        bgcolor = admon_style.get(self.type_, {}).get("bgcolor", "#20222c")
        border_color = admon_style.get(self.type_, {}).get("border_color", "white24")
        icon = admon_style.get(self.type_, {}).get("icon", "white24")

        self.container = ft.Container(
            height=58,
            bgcolor=ft.colors.with_opacity(0.95, bgcolor),
            border_radius=6,
            padding=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        vertical_alignment="center",
                        spacing=10,
                        controls=[
                            ft.Icon(
                                name=icon,
                                color=border_color,
                                size=18,
                            ),
                            ft.Text(
                                self.type_.capitalize(),
                                size=12,
                                weight="w700",
                            ),
                        ],
                    ),
                    ft.IconButton(
                        icon=ft.icons.ADD,
                        icon_size=15,
                        icon_color=border_color,
                        rotate=ft.Rotate(0, ft.alignment.center),
                        animate_rotation=ft.Animation(400, "easeOutBack"),
                        on_click=lambda e: self.resize_admonition(e),
                    ),
                ],
            ),
        )

        super().__init__(
            expand=expand,
            height=height,
            padding=padding,
            border_radius=border_radius,
            animate=animate,
            clip_behavior=clip_behavior,
            border=ft.border.all(0.85, border_color),
            shadow=shadow,
            content=ft.Column(
                alignment="start",
                spacing=0,
                controls=[
                    self.container,
                    self.column,
                ],
            ),
        )

    # method: expand and retract admonition control + animation set
    def resize_admonition(self, e):
        if self.height != self.expanded_height:
            self.height = self.expanded_height
            self.container.border_radius = ft.border_radius.only(topLeft=6, topRight=6)
            e.control.rotate = ft.Rotate(0.75, ft.alignment.center)
        else:
            self.height = 60
            e.control.rotate = ft.Rotate(0, ft.alignment.center)
            self.container.border_radius = 6

        self.update()


class FixedAdmonitions(ft.Container):
    def __init__(
        self,
        type_: str,
        expanded: bool,
        title: str,
        *args,
        **kwargs,
    ):
        self.title = title
        # define admonition title properties
        bgcolor = admon_style.get(type_, {}).get("bgcolor", "#20222c")
        border_color = admon_style.get(type_, {}).get("border_color", "white24")
        icon = admon_style.get(type_, {}).get("icon", "white24")

        fonts = font_scheme.get("admonitions_title", {})
        title_font = fonts.get("font_family")
        title_size = fonts.get("size")

        self.container = ft.Container(
            height=58,
            bgcolor=ft.colors.with_opacity(0.95, bgcolor),
            border_radius=6,
            padding=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        vertical_alignment="center",
                        spacing=10,
                        controls=[
                            ft.Icon(
                                name=icon,
                                color=border_color,
                                size=18,
                            ),
                            ft.Text(
                                type_.capitalize(),
                                size=title_size,
                                font_family=title_font,
                                weight="w700",
                            ),
                            ft.Text(
                                self.title,
                                size=13,
                                font_family=title_font,
                                weight="w400",
                            ),
                        ],
                    ),
                ],
            ),
        )

        # define self instance properties
        kwargs.setdefault(
            "shadow",
            ft.BoxShadow(
                spread_radius=8,
                blur_radius=15,
                color=ft.colors.with_opacity(0.35, "black"),
                offset=ft.Offset(4, 4),
            ),
        )
        kwargs.setdefault("border", ft.border.all(0.85, border_color))
        kwargs.setdefault("clip_behavior", ft.ClipBehavior.HARD_EDGE)
        kwargs.setdefault("animate", ft.Animation(300, "decelerate"))
        kwargs.setdefault("expand", expanded)
        kwargs.setdefault("border_radius", 6)
        kwargs.setdefault("height", 60)
        kwargs.setdefault("padding", 0)
        kwargs.setdefault(
            "content",
            ft.Column(
                alignment="start",
                spacing=0,
                controls=[
                    self.container,
                ],
            ),
        )

        super().__init__(*args, **kwargs)
