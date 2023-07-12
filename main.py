from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, BooleanProperty

class WidgetsExample(GridLayout):
    
    count = NumericProperty(1)
    my_text = StringProperty("1")
    is_count_disabled = BooleanProperty(False)
    slider_value = StringProperty("1")
    
    def on_button_click(self):
        self.count += 1
        self.my_text = str(self.count)
        
    def on_toggle_button_click(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.is_count_disabled = True
        elif widget.state == "down":
            widget.text = "ON"
            self.is_count_disabled = False
            
    def on_slider_value_changed(self, widget):
        self.slider_value = str(int(widget.value))          
        


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            #size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

#class GridLayoutExample(GridLayout):
#    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
