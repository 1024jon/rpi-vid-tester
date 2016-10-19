import kivy
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle


class MyApp(App):

    def build(self):
        # Set up the layout:
        layout = GridLayout(cols=4, spacing=30, padding=30, row_default_height=30)

        # Make the background gray:
        with layout.canvas.before:
            Color(.2,.2,.2,1)
            self.rect = Rectangle(size=(800,600), pos=layout.pos)

        # Instantiate the first UI object (the GPIO input indicator):
        btn1 = Button(text="Input")
        btn2 = Button(text="Input")
        btn3 = Button(text="Input")
        btn4 = Button(text="Input")
        btn5 = Button(text="Input")
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)



        return layout

if __name__ == '__main__':
    MyApp().run()