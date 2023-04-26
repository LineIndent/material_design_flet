import click


@click.command()
@click.argument("project_name")
def init_code(project_name):
    """
    Create a new Flet Material project with a main.py file.
    """
    template_code = """import flet as ft
import flet_material as fm

# begin by changing your app theme color here ...
fm.Theme.set_theme(theme="blue")

def main(page:ft.Page):
    page.bgcolor = fm.Theme.bgcolor
    page.update()

if __name__ == "__main__":
    ft.flet.app(target=main)
"""

    with open(f"{project_name}/main.py", "w") as f:
        f.write(template_code)

    click.echo(f"Created {project_name}/main.py")


if __name__ == "__main__":
    init_code()
