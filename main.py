import kivy
import subprocess
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label

def crosshatch(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/crosshatchvid.sh')
def overscan(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/overscanvid.sh')  
def set1080(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1080.sh')    
def set720(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set720.sh')    


class MyApp(App):
    

    def build(self):
        # Set up the layout:
        layout = GridLayout(cols=4, spacing=30, padding=30, row_default_height=20)

        # Make the background gray:
        with layout.canvas.before:
            Color(.2,.2,.2,1)
            self.rect = Rectangle(size=(800,600), pos=layout.pos)

        btn1 = Button(text="Crosshatch")
        btn1.bind(on_press=crosshatch)
        btn2 = Button(text="Overscan")
        btn2.bind(on_press=overscan)
        btn3 = Button(text="1080p")
        btn3.bind(on_press=set1080)
        btn4 = Button(text="720p")
        btn4.bind(on_press=set720)
        btn5 = Button(text="Input")
        
        layout.add_widget(Label(text="Test Video"))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)



        return layout

if __name__ == '__main__':
    MyApp().run()
