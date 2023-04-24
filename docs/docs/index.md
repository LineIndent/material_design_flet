# **Welcome to<span style="color:cyan; font-weight: extrabold;"> Flet Material Library</span>**

## Getting Started

<span style="color:cyan">Flet Material Library</span> is a material theme built for [Flet](https://flet.dev/docs/) framework, which allows building interactive multi-user web, desktop, and mobile applications in your favorite language without prior experience in frontend development. If you're already familiar with Flet, then you can easily implement the following library to make your applications modern, professional, and eye-catching. 

## Installation Guide

### Python PIP Package
Currently you can get Flet Material Library by using the popular Python package manager `pip`.
Ideally, you'll want to install this, as well as the main Flet library in a virtual environment. Open up a terminal and enter the following command:

    pip install flet-material

!!! warning "Warning: Python Version Compatibility"
    Please note that Flet requires Python 3.7 or higher. If you're using an older version of Python, you may encounter errors when trying to use Flet. Additionally, some of the features of Flet may not be available in older versions of Python. Therefore, we recommend that you ensure your Python installation is up-to-date before attempting to use Flet.


### GitHub Clone

To clone the ***material_design_flet*** repository from GitHub, open a terminal or command prompt and navigate to the directory where you want to store the cloned repository. Then, run the following command:

    git clone https://github.com/LineIndent/material_design_flet.git

This will download the repository to your local machine, and you can then start using the material design components in your Flet-based Python applications.


## Application Setup

Once the library is installed successfully on your system, create a ***main.py*** file in the desired directory. Then, implement the following code in your file:

=== "***main.py***"

    ```py linenums="1"
    # Core modules for your application
    import flet as ft
    import flet_material as fm

    # Set your application theme
    fm.Theme.set_theme(theme="blue")

    # Your main method with all your components
    def main(page: ft.Page):
        page.bgcolor = fm.Theme.bgcolor

        page.update()

    if __name__ == "__main__":
        ft.flet.app(target=main)

    ```

You now have access to all the material design components in your application!


## Next Steps?
If your setup is complete, there are a few things you can do:

!!! tip "What's Next?"
    - Visit the [Line Indent YouTube Channel]() and check out any relevant videos for your current project.
    - Explore the [navigation pannel]() above for library specific projects. I've tried to best explain the code here to make the programming experience easier.
    - See a project you're intrested in and want to clone it? Visit the channel's [GitHub]() to easily access content for your softeware development project.
    - You can also report issues or bugs through the GitHub repository. 

