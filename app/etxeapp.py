from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<Pantaila>:
    BoxLayout:
        orientation: "vertical"
        height:root.height
        width:root.width
        BoxLayout:
            orientation: "horizontal"
            height:root.height/4
            width:root.width
            Label:
                text: "kaixo"
            Button:
                text: "kaixo"
        BoxLayout:
            orientation: "horizontal"
            height:root.height
            width:root.width
        BoxLayout:
            orientation: "horizontal"
            height:root.height/6
            width:root.width
        BoxLayout:
            orientation: "horizontal"
            height:root.height/6
            width:root.width
        BoxLayout:
            orientation: "horizontal"
            height:root.height/6
            width:root.width
        BoxLayout:
            orientation: "horizontal"
            height:root.height/4
            width:root.width
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