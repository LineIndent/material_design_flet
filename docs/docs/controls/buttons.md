# Buttons

Buttons are one of the most common UI elements used in applications. They are used to trigger actions, such as submitting a form or navigating to a different part of the application. Buttons can be designed in various styles, such as flat or raised, and can have different shapes and sizes depending on their purpose.


The ***buttons*** class is straightforward and easy to use. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic Button Example</span>

!!! tip "Flet Material Button Class"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, the ***fm.Buttons()*** class inherits from Flet's ***ft.Container()*** class, this means all properties of the latter are accessable through the former. 

=== "*Buttons*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        button = fm.Buttons(
            width=220,
            height=55,
            title="Give this repo a star!",
        )

        page.add(button)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***width: int -*** The width of the button.

    ***height: int -*** The height of the button.

    ***title: str -*** The text to be displayed inside the button.


