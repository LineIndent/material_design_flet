# Chips

Chips are small UI elements used to display small amounts of information in a compact way. They can be used to show user information, such as a profile picture or name, or to display tags or categories. Chips can be designed in various shapes and sizes, and can be used to represent different types of data.


The ***chips*** class is straightforward and easy to use. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic Chips Example</span>

!!! tip "Flet Material Chips"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, the ```fm.FilterChip()``` class inherits from Flet's ```ft.Container()``` class, this means all properties of the latter are accessable through the former. 

=== "*Chips*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        chip = fm.FilterChip(title="Hello World!", chip_width=123)

        page.add(chip)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***title: str -*** The title to be displayed. 
    
    ***width: int -*** Set the width to accomodate both controls. 