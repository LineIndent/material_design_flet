# Switches

Switches are UI elements that allow users to toggle between two states, typically on and off. They are often represented as a small rectangular or circular button with a sliding mechanism that moves from one side to the other when toggled. Switches are popular in mobile and desktop applications due to their simplicity and ease of use.


The ***switches*** class is straightforward and easy to use. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic Switch Example</span>

!!! tip "Flet Material Switches"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, the ```fm.Switches()``` class inherits from Flet's ```ft.Container()``` class, this means all properties of the latter are accessable through the former. 

=== "*Switches*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        switch = fm.Switchs()

        page.add(switch)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```
