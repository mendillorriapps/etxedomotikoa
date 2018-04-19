from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.image import Image
from kivy.properties import ObjectProperty

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<Konfigurazioa>:
    alarma_box: alarma
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
        BoxLayout:
            orientation: "horizontal"
            height:root.height/2
            width:root.width
            Image:
                source: '.png'
        BoxLayout:
            orientation: "horizontal"
            height:root.height/4
            width:root.width
            Image:
                source: ".png"
        GridLayout:
            orientation: "horizontal"
            cols: 2
            height:root.height
            width:root.width
            Image:
                source: 'argia.png'
            Switch:
                on_active: root.argia("argia")
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
            id:alarma
            orientation: "horizontal"
            cols: 2
            height:root.height/6
            width:root.width
            Image:
                source: 'alarma.gif'
            Switch:
""")

# Declare both screens
class Konfigurazioa(Screen):

    alarma_box = ObjectProperty(None)

    def atzera(self):
        print("Atzera")
        sm.current = "Konfigurazioa"

    def funtzioa(self):
        print("botoia")

    def argia(self,switch):
        print(switch)
        self.alarma_box.size_hint_y=None
        self.alarma_box="0dp"



# Create the screen manager
sm = ScreenManager()
sm.add_widget(Konfigurazioa(name='Konfigurazioa'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
