import kivy
import subprocess
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.scrollview import ScrollView

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        with layout.canvas.before:
            Color(.2,.2,.2,1)
            self.rect = Rectangle(size=(800,600), pos=layout.pos)  
            
        with open("/home/pi/edid.txt") as f:
            contents = f.read()
            main_label = Label(text=contents, font_size='8sp')
            
            layout.add_widget(main_label)
            
            return layout
        
if __name__ == '__main__':
    MyApp().run()