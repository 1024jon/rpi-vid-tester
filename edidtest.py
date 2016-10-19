import kivy
import subprocess
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))
with open("/home/pi/rpi-vid-tester/edid.txt") as f:
    contents = f.read()
    layout.add_widget(Label(text=contents))

root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)
        
runTouchApp(root)