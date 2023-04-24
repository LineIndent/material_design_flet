# Alerts

Alerts are commonly used to provide users with important information, such as warnings or errors, that require their attention. They can be designed to be visually prominent, with attention-grabbing colors and animations, to ensure that the user notices them. Alerts can also be used to confirm a successful action or completion of a task.


The ***alerts*** class is straightforward and easy to use. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic Alerts Example</span>

!!! tip "Flet Material Alerts"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, the ```fm.Alerts()``` class inherits from Flet's ```ft.Container()``` class, this means all properties of the latter are accessable through the former. 

=== "*Alerts*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        alert = fm.Alerts(
            type_="info",
            size="lg",
            title="Did you know?",
            comment="Now you know what you know.",
        )
        page.add(alert)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***type_: str -*** The type of alert to be displayed.

        - "info": displays a blue-colored alert.
        - "warn": displays a yellow-colored alert.
        - "question": displays a green-colored alert.

    ***size: str -*** Sets the width dimension of the alert.

        - "sm": sets width at 250.
        - "md": sets width at 300.
        - "lg": 350.

    ***title: str -*** The title to be displayed. This is the first row. 
    
    ***comment: str -*** The message to be displayed. This is the second row. 