import flet as ft

admonition_style: dict = {
    "height": 60,
    "padding": 0,
    "border_radius": 6,
    "animate": ft.Animation(300, "decelerate"),
    "clip_behavior": ft.ClipBehavior.HARD_EDGE,
    "shadow": ft.BoxShadow(
        spread_radius=8,
        blur_radius=15,
        color=ft.colors.with_opacity(0.35, "black"),
        offset=ft.Offset(4, 4),
    ),
}
