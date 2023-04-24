# CheckBoxes

Checkboxes are used to allow users to select one or multiple options from a set of choices. They are commonly used in forms and settings menus to allow users to customize their preferences. Checkboxes can be designed in various styles, such as with a checkmark or a filled-in box, to provide visual feedback to the user.


The ***checkbox*** class is straightforward and easy to use. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic CheckBox Example</span>

!!! tip "Flet Material CheckBox"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, the ```fm.CheckBox()``` class inherits from Flet's ```ft.Container()``` class, this means all properties of the latter are accessable through the former. 

=== "*Checkboxes*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        circle_checkbox = fm.CheckBox("circle")
        rectangular_checkbox = fm.CheckBox("rectangle")

        page.add(circle_checkbox)
        page.add(rectangular_checkbox)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***shape: str -*** The shape of the checkbox.

        - "circle": The checkbox is a circle.
        - "rectangle": The checkbox is a rectangle with no border adjustments.
