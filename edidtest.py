import kivy
import subprocess
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.scrollview import ScrollView

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
                   
        with open("/home/pi/edid.txt") as f:
            contents = f.read()
            main_label = Label(text=contents)
            layout.add_widget(main_label)
            
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
            

        root.add_widget(layout)
            
        return root
        
if __name__ == '__main__':
    MyApp().run()