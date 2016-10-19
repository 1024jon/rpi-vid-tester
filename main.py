import kivy
import subprocess
kivy.require('1.9.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

def general(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/generalvid.sh')
def crosshatch(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/crosshatchvid.sh')
def overscan(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/overscanvid.sh')  
def avsync(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/avsyncvid.sh')    
def colorbars601(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/colorbars601.sh')       
def colorbars709(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/colorbars709.sh')  
    
def set1080(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1080.sh')  
def set1080i(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1080i.sh')  
def set720(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set720.sh')  
def set480(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set480.sh')  
def set1680(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1680.sh')  
def set1360(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1360.sh')  
    
def set12801024(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set12801024.sh')  
def set1280960(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1280960.sh')  
def set1366(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1366.sh')  
def set1920(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1920.sh')  
def set1440(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1440.sh')  
def set1400(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/set1400.sh')  
    
def readedid(instance):
    subprocess.Popen('/home/pi/rpi-vid-tester/readedid.sh') 
    with open("/home/pi/edid.txt") as f:
        contents = f.read()    
        popup = Popup(title=contents,
                      content=Label(text='EDID', font_size='8sp'),
                      size_hint=(None, None), size=(400, 600))    
    


class MyApp(App):
    

    def build(self):
        # Set up the layout:
        layout = GridLayout(cols=7, spacing=10, padding=10, row_default_height=20)

        # Make the background gray:
        with layout.canvas.before:
            Color(.2,.2,.2,1)
            self.rect = Rectangle(size=(800,600), pos=layout.pos)

        btn1 = Button(text="General")
        btn1.bind(on_press=general)                
        btn2 = Button(text="Crosshatch")
        btn2.bind(on_press=crosshatch)
        btn3 = Button(text="Overscan")
        btn3.bind(on_press=overscan)
        btn4 = Button(text="Avsync")
        btn4.bind(on_press=avsync)      
        btn5 = Button(text="ColorBars601")
        btn5.bind(on_press=colorbars601)
        btn6 = Button(text="ColorBars709")
        btn6.bind(on_press=colorbars709)        
        
        
        btn7 = Button(text="1080p60")        
        btn7.bind(on_press=set1080)
        btn8 = Button(text="1080i60")
        btn8.bind(on_press=set1080i)        
        btn9 = Button(text="720p60")
        btn9.bind(on_press=set720)
        btn10 = Button(text="480p60")
        btn10.bind(on_press=set480)
        btn11 = Button(text="1680x1050")
        btn11.bind(on_press=set1680)          
        btn12 = Button(text="1360x768")
        btn12.bind(on_press=set1360)
        
        btn13 = Button(text="1280x1024")
        btn13.bind(on_press=set12801024)        
        btn14 = Button(text="1280x960")
        btn14.bind(on_press=set1280960)   
        btn15 = Button(text="1366x768")
        btn15.bind(on_press=set1366)   
        btn16 = Button(text="1920x1200")
        btn16.bind(on_press=set1920)  
        btn17 = Button(text="1440x900")
        btn17.bind(on_press=set1440)   
        btn18 = Button(text="1400x1050")
        btn18.bind(on_press=set1400)         

        
        
        btn19 = Button(text="Read EDID")
        btn19.bind(on_press=readedid)
        
        layout.add_widget(Label(text="Test Videos ->", font_size="12sp"))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)

        layout.add_widget(Label(text="Primary Resolutions ->", font_size="12sp"))
        layout.add_widget(btn7)
        layout.add_widget(btn8)
        layout.add_widget(btn9)
        layout.add_widget(btn10)
        layout.add_widget(btn11)
        layout.add_widget(btn12)
        
        layout.add_widget(Label(text="Odd Resolutions ->", font_size="12sp"))
        layout.add_widget(btn13)
        layout.add_widget(btn14)
        layout.add_widget(btn15)
        layout.add_widget(btn16)
        layout.add_widget(btn17)
        layout.add_widget(btn18)

        layout.add_widget(Label(text="Other --->", font_size="12sp"))
        layout.add_widget(btn19)


        return layout

if __name__ == '__main__':
    MyApp().run()
