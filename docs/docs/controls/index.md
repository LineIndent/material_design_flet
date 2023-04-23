# Configuration

Flet Material Library has many customized controls that can be used in your Flet-based applications. This section of the documentation will go through the steps to customize your app's theme, which will set the appropriate settings for the rest of the controls. 

# Setting the theme in your Flet application

## Application setup
Before selecting your application theme color, make sure the following line of code is included in your main script:

``` py
fm.Theme.set_theme(theme="")
```

## Choosing a theme color
Below you'll find all the  supported theme colors offered Flet Material Library. Once you've decided on a theme, you can set it in your Flet application like this:



``` py
fm.Theme.set_theme(theme="indigo")
```

!!! warning "The theme argument is case sensitive - all colors names should be lower case and with spaces!"


<style>
    .color-boxes {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .color-box {
        flex: 1 0 calc(20% - 10px); /* each box takes up 20% of the available space, minus the margin between boxes */
        margin: 5px; /* set the margin between boxes */
        height: 60px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 6px

    }
</style>

<div class="color-boxes">
    <div class="color-box" style="background-color: #dd6058;">Red</div>
    <div class="color-box" style="background-color: #d63863;">Pink</div>
    <div class="color-box" style="background-color: #a855f7;">Purple</div>
    <div class="color-box" style="background-color: #4f46e5;">Indigo</div>
    <div class="color-box" style="background-color: #3b82f6;">Blue</div>
    <div class="color-box" style="background-color: #0ea5e9;">Light Blue</div>
    <div class="color-box" style="background-color: #06b6d4;">Cyan</div>
    <div class="color-box" style="background-color: #14b8a6;">Teal</div>
    <div class="color-box" style="background-color: #22c55e;">Green</div>
    <div class="color-box" style="background-color: #84cc16;">Lime</div>
    <div class="color-box" style="background-color: #eab308;">Yellow</div>
    <div class="color-box" style="background-color: #f59e0b;">Amber</div>
    <div class="color-box" style="background-color: #f97316;">Orange</div>
    <div class="color-box" style="background-color: #78716c;">Earth</div>
    <div class="color-box" style="background-color: #64748b;">Slate</div>
    <div class="color-box" style="background-color: #000000;">Black</div>
    <div class="color-box" style="background-color: #ffffff; color: black">White</div>
</div>

Now that you've set up your theme color, you can easily implement the controls you want inside your flet application. Visit each control page to get more details on their properties. 