from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from LoginView import LoginView
class SimpleApp(MDApp):
    def build(self):
        login_view=LoginView()
        mainScreen= login_view.show()
        return mainScreen
SimpleApp().run()
