# from kivy.config import Config
# Config.set('graphics', 'width', '700')  # Set width to 800 pixels
# Config.set('graphics', 'height', '350')
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
# from kivy.core.window import Window
# Window.size=(500,300)
from helper import expensetracker
import Signup



class LoginView(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        E_Tracker=Builder.load_string(expensetracker) 
        return E_Tracker
    def signup_window(self,obj):
          pass
    def show(self,obj):
            if self.u_text_field.text is "":
                 check_string="Please enter a username"
            else:
                 check_string=self.u_text_field.text+" does not exist."
            close_button=MDFlatButton(text="Close",on_release=self.close)
            more_button=MDFlatButton(text="More")
            self.dialog=MDDialog(title="Username Check",text=check_string,
                            size_hint=(0.5,1),
                            buttons=[close_button,more_button])
            self.dialog.open()
    def close(self,obj):
         self.dialog.dismiss()
LoginView().run()    
