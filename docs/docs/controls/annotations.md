# Annotations

Annotations, much like tootips, are used to provide additional context or information about a UI element. They can be used to provide instructions or tips for using a particular feature or to label specific parts of an interface. Annotations can also be used to indicate the status of an element, such as whether it is currently active or disabled.


The ***annotations*** class is straightforward and easy to use. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic Annotation Example</span>

!!! tip "Flet Material Annotations"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, the ```fm.Annotations()``` class inherits from Flet's ```ft.Container()``` class, this means all properties of the latter are accessable through the former. 

=== "*Annotations*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm

    def main(page: ft.Page):

        page.bgcolor = fm.Theme.bgcolor

        annotation = fm.Annotations("This is an annotated message!")
        
        page.add(annotation)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***annotations_msg: str -*** The content to be shown when annotation is hovered. 
