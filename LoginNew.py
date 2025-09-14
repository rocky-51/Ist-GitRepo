# Code of Python Program
from kivy.core.window import Window
Window.size=(500,300)
from kivymd.app import MDApp
from kivy.lang import Builder
import MyApp
class Myapp(MDApp):
    def build(self):
        a=Builder.load_string(MyApp.KV)
        return a

Myapp().run()