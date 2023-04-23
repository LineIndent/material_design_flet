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


<!-- ??? info "Main Objectives"

    * [x] Provide additional resources and materials to supplement the video tutorials, such as written explanations, code samples, and links to relevant documentation and tools.
    * [x] Create a community hub where viewers can connect with each other, ask questions, and share their own projects and experiences.
    * [x] Offer premium content or courses for viewers who want to dive deeper into specific topics or receive more personalized instruction.
    * [x] Showcase the channel's portfolio of completed projects and provide contact information for potential clients or collaborators.
    * [x] Generate revenue through advertising, sponsorships, or affiliate marketing by attracting visitors to the website and building a loyal following.

## **The topics covered**

The topics covered on this channel range from building modern-looking applications to learning a wide range of programming concepts. Python is the primary language used, but other languages are covered as well.

=== "Python"
    -  Python is a high-level, interpreted programming language that is popular for its simplicity, readability, and ease of use.
    -  It has a large and active community that contributes to its many libraries and frameworks.

=== "Desktop/Mobile Apps"
    -  Python can be used to build desktop and mobile applications using libraries like **==Flet==** and **==Pynecone==**.
    -  It provides an easy-to-use interface for creating GUI applications and has support for cross-platform development.

=== "Data Analysis"
    -  Python has become a popular language for data analysis due to its powerful libraries like Pandas, NumPy, and Matplotlib.
    -  It is used for everything from data cleaning and manipulation to statistical modeling and visualization.

=== "Unit Testing"
    -  Python has several frameworks for unit testing, including the built-in unittest module, pytest, and nose.
    -  These frameworks allow developers to write automated tests to ensure their code is working as expected.

=== "CI/CD"
    -  Continuous integration and continuous deployment (CI/CD) is a process that involves continuously building, testing, and deploying code.
    -  Python has several tools and frameworks like Jenkins and Travis CI that can be used to set up and automate CI/CD pipelines.

=== "Game Development"
    - Python can be used for game development using libraries like Pygame and PyOpenGL.
    -  While it may not be as performant as some other languages, it can be a good choice for prototyping and creating 2D games.

## Getting started

To follow along with the common theme of the channel, you can use the following steps to see if your setup is complete.

### Installing Python

#### macOS & Linux
>
> Python is pre-installed on macOS and most Linux distributions. To check if Python is installed, open a terminal window and type:

    python --version

#### Windows
>
> To install Python on Windows, you can download the installer from the official Python website:

>[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

### Installing Flet Library

!!! warning "Warning: Python version compatibility"
    Please note that Flet requires Python 3.7 or higher. If you're using an older version of Python, you may encounter errors when trying to use Flet. Additionally, some of the features of Flet may not be available in older versions of Python. Therefore, we recommend that you ensure your Python installation is up-to-date before attempting to use Flet.

#### macOS

!!! info "Flet installation on macOS"
    Open a terminal or activate a virtual environment and run the following command:
    ```
    pip3 install flet
    ```
    To upgrade the Flet library, run the following:
    ```
    pip3 install flet --upgrade
    ```

#### Windows

!!! info "Flet installation on Windows"
    ```
    pip install flet
    ```

#### Linux

!!! info "Flet installation on Linux"
    Visit the following link for detailed instructions:

    ```
    https://flet.dev/docs/guides/python/getting-started#linux
    ```

### Installing Pynecone Library

!!! warning "Warning: Python version compatibility"
    Pynecone requires at least Python 3.5. If you are using an older version of Python, you will need to upgrade to use this package. Using an outdated version of Python may result in compatibility issues and security vulnerabilities. We recommend upgrading to the latest version of Python to ensure optimal performance and security.

#### macOS, Windows, & Linux

1. Open your terminal application.

2. Install Python3 if it is not already installed on your system. You can download the latest version of Python3 from the official website: <https://www.python.org/downloads/>.

3. Install Pynecone using pip by running the following command:

```
python3 -m pip install pynecone
```

4. Verify that Pynecone has been installed by running the following command:

```
python3 -c "import pynecone"
```

### Other Dependencies

Below are a few other dependencies that are typically used accross the projects and videos on this channel. While they are not always necessary, having them in a virtual environment can facilitate the development process.

#### Installing Pyrebase (Firebase API Wrapper)

!!! info "Pyrebase Module"
    Pyrebase is a Python library that serves as a Firebase API wrapper. It provides a simple interface for Python developers to interact with Firebase services such as the real-time database, authentication, and storage. Pyrebase allows developers to easily use Firebase services in their Python applications.

    === "macOS & Linux"
        ```
        pip3 install pyrebase4
        ```

    === "Windows"
        ```
        pip3 install pyrebase4
        ```

#### Installing Aiosqlite (Asynchronous SQLite Support)

!!! info "Aiosqlite Module"
    Aiosqlite is an asynchronous wrapper for the built-in SQLite3 library in Python. It allows developers to use SQLite3 in their asyncio-based applications and supports various SQLite3 features such as transactions, row factory, and query execution. aiosqlite makes it easy for developers to use SQLite3 in their async applications by providing a simple and efficient interface for SQLite3 operations.

    === "macOS & Linux"
        ```
        pip install aiosqlite
        ```

    === "Windows"
        ```
        pip install aiosqlite
        ```

#### Installing Flask (Python Web Framework)

!!! info "Flask Library"
    Flask is a lightweight and flexible web framework for Python that allows developers to quickly build web applications. It provides a simple and elegant way to handle web requests, template rendering, and other web-related tasks. With Flask, developers can create web applications with minimal boilerplate code and can easily extend its functionality using various Flask extensions available.

    === "macOS & Linux"
        1. Create a new directory.
        ```
        mkdir flask-app
        ```
        2. Change into the directory.
        ```
        cd flask-app
        ```
        3. Create a virtual environment.
        ```
        python3 -m venv envFlask
        ```
        4. Activate the virtual environment.
        ```
        source envFlask/bin/activate
        ```
        5. Install Flask.
        ```
        pip3 install flask
        ```

    === "Windows"
        1. Create a new directory.
        ```
        mkdir flask-app
        ```
        2. Change into the directory.
        ```
        cd flask-app
        ```
        3. Create a virtual environment.
        ```
        py -3 -m venv envFlask
        ```
        4. Activate the virtual environment.
        ```
        envFlask\Scripts\activate
        ```
        5. Install Flask.
        ```
        pip3 install flask
        ```

### What's Next?

If your setup is complete, there are a few things you can do from here.

!!! tip "What's Next?"
    - Visit the [Line Indent YouTube Channel]() and check out any relevant videos for your current project.
    - Explore the [navigation pannel]() above for library specific projects. I've tried to best explain the code here to make the programming experience easier.
    - See a project you're intrested in and want to clone it? Visit the channel's [GitHub]() to easily access content for your softeware development project.
    - Enjoyed the content? Consider [supporting the channel]() for it to continue to grow and create new content. -->