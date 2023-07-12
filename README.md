# Introduction to kivy - [Official Doc](https://kivy.org/doc/stable/)

Course developed by Jonathan Roux : [Youtube Reference](https://www.youtube.com/watch?v=l8Imtec4ReQ&ab_channel=freeCodeCamp.org)

To install kivy use:
> pip install kivy

---

## Kivy Design Language
Kivy provides a design language specifically geared towards easy and scalable GUI Design. The language makes it simple to separate the interface design from the application logic, adhering to the separation of concerns principle.

The kivy file has `.kv` extension

---
## Properties
[Documentation](https://kivy.org/doc/stable/gettingstarted/properties.html)

Properties implements Observer Pattern.

> NumericProperty, StringProperty, ListProperty, ObjectProperty, BooleanProperty, BoundedNumericProperty, OptionProperty, ReferenceListProperty, AliasProperty, DictProperty, VariableListProperty, ConfigParserProperty, ColorProperty

---

## Layouts
[Documentation](https://kivy.org/doc/stable/gettingstarted/layouts.html)
1. BoxLayout: Widgets are arranged sequentially, in either a ‘vertical’ or a ‘horizontal’ orientation.
2. AnchorLayout: Widgets can be anchored to the ‘top’, ‘bottom’, ‘left’, ‘right’ or ‘center’.
3. GridLayout: Widgets are arranged in a grid defined by the rows and cols properties.
4. StackLayout: Widgets are stacked in a lr-tb (left to right then top to bottom) or tb-lr order.
5. PageLayout: Used to create simple multi-page layouts, in a way that allows easy flipping from one page to another using borders.
6. FloatLayout: Widgets are essentially unrestricted.
7. RelativeLayout: Child widgets are positioned relative to the layout.
8. ScatterLayout: Widgets are positioned similarly to a RelativeLayout, but they can be translated, rotated and scaled.

ScrollView : It is not a layout but use to have a scroll horizontally or vertically by adding child layout. It can hold single child layout.

---

## Widgets
1. Button
2. ToggleButton
3. Switch
4. Slider
5. ProgressBar
6. TextInput
7. Image

