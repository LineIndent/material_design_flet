import flet as ft
import flet_material as fm


fm.Theme.set_theme(theme="blue")


def main(page: ft.Page):
    # note = fm.Admonitions(
    #     type_="",
    #     expanded_height=300,
    #     expand=False,
    #     controls_list=None,
    # )

    # custom = fm.FixedAdmonitions("tip", False)
    # custom1 = fm.FixedAdmonitions("success", False)
    # custom2 = fm.FixedAdmonitions("warning", False)
    # custom3 = fm.FixedAdmonitions("danger", False)
    # custom4 = fm.FixedAdmonitions("info", False)
    # custom5 = fm.FixedAdmonitions("abstract", False)

    # page.add(note)
    # page.add(custom)
    # page.add(custom1)
    # page.add(custom2)
    # page.add(custom3)
    # page.add(custom4)
    # page.add(custom5)

    chip = fm.FilterChip(title="Dragon Den", width=120)
    switch = fm.Switchs()
    check = fm.CheckBox("rectangle")

    page.add(chip)
    page.add(switch)
    page.add(check)

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
