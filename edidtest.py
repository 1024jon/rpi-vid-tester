import kivy
import subprocess
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='left', anchor_y='bottom')
        with open("/home/pi/edid.txt") as f:
            contents = f.read()
            main_label = Label(text=contents)
            
            layout.add_widget(main_label)
            
            return layout
        
if __name__ == '__edidtest__':
    MyApp().run()