import flet as ft

import flet_material as fm


fm.Theme.set_theme(theme="cyan")

global count
count = 0


def main(page: ft.Page):
    page.bgcolor = "#2e2f3e"
    page.padding = 30

    def simulate_notification(e):
        global count
        count += 1
        badge.add_notification(count)
        icon_badge.add_notification(count)
        page.update()

    box = fm.CheckBox()
    btn = fm.Buttons(
        width=280,
        height=50,
        title="Subscribe to our newsletter",
        on_click=lambda e: simulate_notification(e),
    )
    chip = fm.FilterChip("Rabbit Island", width=120)

    badge = fm.NotificationBadge(title="", size="md")
    icon_badge = fm.IconBadge("notification")
    page.add(badge)
    page.add(icon_badge)

    switch = fm.Switchs()

    page.add(box)
    page.add(btn)
    page.add(chip)
    page.add(switch)

    alert = fm.Alerts(
        "info", "lg", "Did you know?", "Here is something that you might like to know."
    )
    page.add(alert)

    admonition = fm.Admonitions(
        admonitions_type="note",
        expand=True,
        admonitions_end_height=350,
        admonitions_list=[
            ft.Text("asdasdasd", color="white"),
            ft.Container(width=100, height=100, bgcolor="pink"),
        ],
    )

    # page.add(
    #     ft.Row(
    #         controls=[admonition],
    #     )
    # )

    page.update()


if __name__ == "__main__":
    count = 0
    ft.flet.app(target=main)
