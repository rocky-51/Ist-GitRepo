from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

class LoginView(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('LoginView.py')
        expenseTrackerLabel = MDLabel(
            text="Expense Tracker",
            halign="center",
            font_style="H1"
        )
        usernamefield = MDTextField(
            hint_text="Enter your username",
            helper_text="This field is required",
            helper_text_mode="on_focus",
            mode="rectangle",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint_x=0.8
        )
        passwordfield=MDTextField(hint_text="Enter Your Password",password=True,password_mask='.')
        btn_flt=MDRectangleFlatButton(text='Hello World',pos_hint={'center_x':0.5,'center_y':0.5})
        signupLabel = MDLabel(
            text="Don't have an account? click here",
            halign="center",
            font_style="H5"
        )
        screen.add_widget(text_field)
        return screen

if __name__ == '__main__':
    LoginView().run()