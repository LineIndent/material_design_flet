import flet as ft
from flet_material.base import Theme
from styles import badge_size_dimensions, badge_icon
import time


class NotificationBadge(ft.Stack, Theme):
    def __init__(
        self,
        title: str,
        size: str,
        notification: int,
        *args,
        **kwargs,
    ):
        # set the start notification counter
        self.notification = notification

        # get the wdiget dimension
        size = badge_size_dimensions.get(size, {})
        width = size.get("width", 55)
        height = size.get("height", 45)

        #
        self.notification_text = ft.Text(
            value=notification, weight="bold", size=9, text_align="center"
        )

        self.notification_box: ft.Control = ft.Container(
            width=22,
            height=22,
            shape=ft.BoxShape("circle"),
            top=0,
            right=0,
            bgcolor="red800",
            border_radius=4,
            offset=ft.transform.Offset(0, -0.25),
            animate_offset=ft.Animation(50, "linear"),
            alignment=ft.alignment.center,
            content=self.notification_text,
        )

        #
        kwargs.setdefault("width", width)
        kwargs.setdefault("height", height)
        kwargs.setdefault(
            "controls",
            [
                ft.Container(
                    width=width * 0.9,
                    height=height * 0.9,
                    bgcolor=Theme.primary_theme,
                    top=1,
                    border_radius=6,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        title,
                        weight="bold",
                        size=12,
                        text_align="center",
                        font_family="Roboto",
                    ),
                ),
                ft.Container(
                    width=25,
                    height=25,
                    top=0,
                    right=0,
                    padding=10,
                    shape=ft.BoxShape("circle"),
                    offset=ft.transform.Offset(0, -0.25),
                    bgcolor="#2e2f3e",
                    alignment=ft.alignment.center,
                ),
                self.notification_box,
            ],
        )

        super().__init__(*args, **kwargs)

    def add_notification(self, current):
        self.notification_text.value = current
        self.notification_box.offset = ft.transform.Offset(0.05, -0.25)
        self.notification_box.update()
        time.sleep(0.05)
        self.notification_box.offset = ft.transform.Offset(-0.05, -0.25)
        self.notification_box.update()
        time.sleep(0.05)
        self.notification_box.offset = ft.transform.Offset(0, -0.25)
        self.notification_box.update()


class IconBadge(ft.Stack, Theme):
    def __init__(
        self,
        bagde_icon: str,
        notification: int,
        *args,
        **kwargs,
    ):
        #
        icon = badge_icon.get(bagde_icon)
        self.notification = notification

        #
        self.notification_text = ft.Text(
            value=notification, weight="bold", size=9, text_align="center"
        )

        self.notification_box: ft.Control = ft.Container(
            width=22,
            height=18,
            top=0,
            right=0,
            bgcolor="red800",
            border_radius=4,
            offset=ft.transform.Offset(-0.30, 0.35),
            animate_offset=ft.Animation(50, "linear"),
            shape=ft.BoxShape("rectangle"),
            alignment=ft.alignment.center,
            content=self.notification_text,
        )

        #
        kwargs.setdefault("width", 64)
        kwargs.setdefault("height", 64)
        kwargs.setdefault(
            "controls",
            [
                self.notification_box,
                ft.Container(
                    width=64 * 0.9,
                    height=64 * 0.9,
                    bgcolor="transparent",
                    top=1,
                    border_radius=6,
                    alignment=ft.alignment.center,
                    content=ft.Icon(name=icon, size=24),
                ),
            ],
        )

        super().__init__(*args, **kwargs)

    def add_notification(self, current):
        self.notification_text.value = current
        self.notification_box.offset = ft.transform.Offset(-0.35, 0.35)
        self.notification_box.update()
        time.sleep(0.05)
        self.notification_box.offset = ft.transform.Offset(-0.25, 0.35)
        self.notification_box.update()
        time.sleep(0.05)
        self.notification_box.offset = ft.transform.Offset(-0.3, 0.35)
        self.notification_box.update()
