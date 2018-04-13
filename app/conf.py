from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.image import Image

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<Pantaila>:
    BoxLayout:
        orientation: "vertical"
        height:root.height
        width:root.width
        canvas.before:
            Color:
                rgba: 0, 255, 0, 0.3
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            orientation: "horizontal"
            height:root.height/4
            width:root.width
        GridLayout:
            orientation: "horizontal"
            cols: 2
            height:root.height
            width:root.width
            Image:
                source: 'argia.png'
            Switch:
        GridLayout:
            orientation: "horizontal"
            cols: 2
            height:root.height/6
            width:root.width
            Image:
                source: 'iturria.png'
            Switch:
        GridLayout:
            orientation: "horizontal"
            cols: 2
            height:root.height/6
            width:root.width
            Image:
                source: 'kalefakzioa.png'
            Switch:
        GridLayout:
            orientation: "horizontal"
            cols: 2
            height:root.height/6
            width:root.width
            Image:
                source: 'alarma.gif'
            Switch:
""")

# Declare both screens
class Pantaila(Screen):

    def atzera(self):
        print("Atzera")

    def funtzioa(self):
        print("botoia")


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Pantaila(name='Froga'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()