# Badges

Badges are used to display small amounts of information, such as notifications or counts, in a visually prominent way. They can be used to indicate the number of new messages, the number of items in a cart, or to show user status, such as whether they are online or offline. Badges can be designed in various styles, such as with a numerical count or an icon.


The ***badges*** class is straightforward and easy to use. There are currently two types of badges, ***notifications*** and ***icon*** bagdes, each having its own unique material design. Choose where you want to place your annotation then create an instance of it, like this:


<span style="font-size:1rem;">Basic Notifications Badge Example</span>

!!! tip "Flet Material Badges"

    The Flet Material Library classes inherit from the controls provided by Flet. In this case, both the ```fm.NotificationBadge()``` and the ```fm.IconBadge()``` classes inherit from Flet's ```ft.Container()``` class, this means all properties of the latter are accessable through the former. 

=== "*Notifications Badge*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        def show_notification(e):
            badge.notification += 1
            badge.add_notification(badge.notification)

        btn = ft.ElevatedButton(on_click=lambda e: show_notification(e))

        badge = fm.NotificationBadge(title="Hello!", size="md", notification=0)

        page.add(badge)
        page.add(btn)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***title: str -*** The text to be displayed.

    ***size: str -*** The width of the notifications badge:

        - "sm": sets the width at 55.
        - "md": sets the width at 90.
        - "lg": sets the width at 135.
        - "xl": sets the width at 165.


    ***notification: int -*** The starting notification count number. 


<span style="font-size:1rem;">Basic Icon Badge Example</span>

=== "*Icon Badge*"

    ``` py linenums="1"
    import flet as ft
    import flet_material as fm


    fm.Theme.set_theme(theme="blue")


    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        def show_notification(e):
            badge.notification += 1
            badge.add_notification(badge.notification)

        btn = ft.ElevatedButton(on_click=lambda e: show_notification(e))

        badge = fm.IconBadge(bagde_icon="email", notification=0)

        page.add(badge)
        page.add(btn)

        page.update()


    if __name__ == "__main__":
        ft.flet.app(target=main)
    ```

=== "*parameters*"

    ***bagde_icon: str -*** The icon to be displayed:

        Supported icons: 
            
            - "email"
            - "facebook"
            - "notification"
            - "cart"

    ***notification: int -*** The starting notification count number. 
    