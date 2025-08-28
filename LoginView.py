from kivy.config import Config
Config.set('graphics', 'width', '700')  # Set width to 800 pixels
Config.set('graphics', 'height', '350')
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from helper import expensetracker,u_textField,p_textField
import Signup



class LoginView(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        E_Tracker=Builder.load_string(expensetracker)
        self.u_text_field=Builder.load_string(u_textField)
        p_text_field=Builder.load_string(p_textField)
        loginButton=MDRectangleFlatButton(text="Login ",
                    pos_hint={ "center_x":.45,"center_y": 0.37,'bottom':0.5,'right':0.8},
                    on_release=self.show)
        s_button=MDFlatButton(text="Don't have an account? Click Here ",
                            pos_hint={"center_x": .5,"center_y": 0.08},
                            theme_text_color="Primary",
                            on_release=self.signup_window)
        screen.add_widget(E_Tracker)
        screen.add_widget(self.u_text_field)
        screen.add_widget(p_text_field)
        screen.add_widget(loginButton)
        screen.add_widget(s_button)
        return screen
    def signup_window(self,obj):
         s_Window=Signup().run()
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
