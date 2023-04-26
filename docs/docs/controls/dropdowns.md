# Dropdown

Dropdowns are used to allow users to select one option from a list of choices. They are commonly used in menus and settings to provide a compact way to present a large number of options. Dropdowns can be designed in various styles, such as with a simple list or with additional information, such as icons or descriptions.


The ***dropdown*** class is straightforward and easy to use. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic Dropdown Example</span>

!!! tip "Flet Material Alerts"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, the ```fm.Admonitions()``` class inherits from Flet's ```ft.Container()``` class, this means all properties of the latter are accessable through the former. 


### Expandable Dropdown

=== "*Expandable Dropdown*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        drop = fm.Admonitions(
            type_="note", expanded_height=300, expanded=False, controls_list=None
        )

        page.add(drop)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***type_: str -*** The type of title to be displayed. The following parameters are supported:

        - "note", "abstract", "info", "tip", "success", "warning", "danger"

    ***expanded_height: int -*** Sets the height when the dropdown is clicked.

    ***expanded: bool -*** If placed outside a ft.Row() or ft.Column(), should be set to ***False***, otherwise set to ***True***. 
    
    ***controls_list: list -*** The list of controls that can be added inside the dropdown. 


### Fixed Dropdown (Title only)

This class simply displays the title and it's corresponding icon. It cannot be expanded. 

=== "*Fixed Dropdown*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        fixed_drop = fm.FixedAdmonitions(
            type_="tip", expanded=False, title="This is type of dropdown is not a dropdown!"
        )

        page.add(fixed_drop)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***type_: str -*** The type of title to be displayed. The following parameters are supported:

        - "note", "abstract", "info", "tip", "success", "warning", "danger"

    ***expanded: bool -*** If placed outside a ft.Row() or ft.Column(), should be set to ***False***, otherwise set to ***True***. 
    
    ***title: str -*** The title to be displayed on top, neaer the icon. 