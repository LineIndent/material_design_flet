<div align="center">
   <a href="[https://squidfunk.github.io/mkdocs-material/](https://flet.dev/)">
   <img src="https://github.com/flet-dev/flet/blob/main/media/logo/Icon-512.png" width="180" height="180" alt="Flet Material Library">
  </a>

**A UI library for Flet framework**

 
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



[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](https://flet-material.vercel.app)


</p>


<p align="center">
Modernize your websites and applications by implementing customized Flet controls that improve user experince and overall visual quality. UI components are flexible and in line with current design trends. 

</p>



## 1. Installation

Flet Material requires the following:


-   Latest version of Flet
-   Python 3.5+

If you don't have Flet isntalled, installing Flet Material automatically installs it for you.
```
$ pip install flet-material
```



## 2. Application Setup

Once you have Flet Material on your system, you can try and run the following code snippet to make sure eveything is working properly:

If you don't have Flet isntalled, installing Flet Material automatically installs it for you.

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

If the package was installed correctly you should see a centered and customized button. 

## 3. Code Breakdown

The script may seem familier because it's very much like the basic Flet application setup. In fact it's the very same with some minor additions.

First, note the import statement at the top of the main file. This is the main library and all its components.
```python
import flet_material as fm
```

Below the imported modules is the ```Theme``` instance from ```flet_material```. This sets up the entire application theme so that all colors, primary and accent, are uniform and the same, giving the applications being built much appeal.

For a list of supported theme colors, you can visit the library's documentation online.

```python
fm.Theme.set_theme(theme="teal")
```

Finally, wihtin the ```main()``` method we have a new control called ```fm.Buttons()```, which simply inherits it's properties from several Flet classes and is customized.

```python
button = fm.Buttons(
    width=220,
    height=55,
    title="Give this repo a star!",
)
```

That's it! You now have access to Flet Material library components!!

## Contributing

Contributions are highly encouraged and welcomed. 


## License

Flet Material Library is open-source and licensed under the [MIT License](LICENSE).





