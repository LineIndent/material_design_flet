<div align="center">
   <a href="[https://squidfunk.github.io/mkdocs-material/](https://flet.dev/)">
   <img src="https://github.com/flet-dev/flet/blob/main/media/logo/Icon-512.png" width="180" height="180" alt="Flet Material Library">
  </a>

**A UI library for Flet**

 
 </div>

<br>
<br>
<p align="center">
  <a href="https://github.com/LineIndent/material_design_flet/actions"><img
    src="https://github.com/LineIndent/material_design_flet/actions/workflows/build.yml/badge.svg?branch=main"
    alt="Build"
  /></a>
  <a href="https://pypistats.org/packages/flet-material"><img
    src="https://img.shields.io/pypi/dm/flet-material.svg"
    alt="Downloads"
  /></a>
  <a href="https://pypi.org/project/flet-material"><img
    src="https://img.shields.io/pypi/v/flet-material.svg"
    alt="Python Package Index"
  /></a>

<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/flet-material">



</p>

<p align="center">
  <a href="https://flet-material.vercel.app"><img
    src="https://img.shields.io/badge/docs-available-brightgreen.svg"
    alt="Docs"
  /></a>

  </p>

<p align="center">
Modernize your websites and applications by implementing customized Flet controls that improve user experience and overall visual quality. The UI components are flexible and aligned with current design trends.
</p>



## 1. Installation

To use Flet Material, you need to have the following installed:

-   Latest version of Flet
-   Python 3.5+

If you don't have Flet installed, installing Flet Material automatically installs it for you. You can install Flet Material using the following command:
```
$ pip install flet-material
```



## 2. Application Setup

After installing Flet Material, you can test if it's working properly by running the following code snippet:

```python
import flet as ft
import flet_material as fm

fm.Theme.set_theme(theme="teal")

def main(page: ft.Page):
   page.bgcolor = fm.Theme.bgcolor

   page.horizontal_alignment = "center"
   page.vertical_alignment = "center"

   button = fm.Buttons(
       width=220,
       height=55,
       title="Give this repo a star!",
   )

   page.add(button)

   page.update()


if __name__ == "__main__":
   ft.flet.app(target=main)
```

If the package was installed correctly, you should see a centered and customized button.

## 3. Code Breakdown

The script is similar to the basic Flet application setup, with some minor additions.

At the top of the main file, you need to import the Flet Material library and all its components:
```python
import flet_material as fm
```

Below the imported modules is the Theme instance from Flet Material. It sets up the entire application theme so that all colors, primary and accent, are uniform, giving the applications being built a consistent look and feel. For a list of supported theme colors, you can visit the library's documentation online.

For a list of supported theme colors, you can visit the library's documentation online.

```python
fm.Theme.set_theme(theme="teal")
```

Finally, within the main() method, you can use a new control called fm.Buttons(), which inherits its properties from several Flet classes and can be customized to your liking:

```python
button = fm.Buttons(
    width=220,
    height=55,
    title="Give this repo a star!",
)
```

That's it! You now have access to Flet Material library components!

## Contributing

Contributions are highly encouraged and welcomed. Check out the [contributon section](https://flet-material.vercel.app/contribute/) of the documentation for more details. 


## License

Flet Material Library is open-source and licensed under the [MIT License](LICENSE).





