from kivy.config import Config
Config.set('graphics', 'width', '700')  # Set width to 800 pixels
Config.set('graphics', 'height', '350')
from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
# from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

expensetracker="""
MDLabel:
    text:"Expense Tracker"
    font_style:"H3"
    pos_hint:{'top':1.3}
    halign:'center'
    valign:'top'
    theme_text_color:"Hint"
"""

u_textField="""
MDTextField:
    hint_text:"Enter Email "
    size_hint_x: None
    width: "200dp"
    valign:'top'
    pos_hint: {'bottom':0.5,"center_x": .5, "center_y": .5}
    mode:'rectangle'
"""
p_textField="""
MDTextField:
    hint_text:"Enter Password "
    size_hint_x: None
    width: "200dp"
    pos_hint: {"center_x": .5, "center_y": .2,'top':0.35,'bottom':0.5}
    mode:'rectangle'
"""
l_button="""
MDFlatButton:
    text:"Login "
    pos_hint:{ "center_x":.45,"center_y": 0.37,'bottom':0.5,'right':0.8}
"""
signupLabel="""
MDLabel:
    text:"Don't have an account? Click Here "
    font_style:"Subtitle2"
    pos_hint:{"center_x": .85,'top':0.6}
    theme_text_color:"Primary"
"""


class LoginView(MDApp):
    def show(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        E_Tracker=Builder.load_string(expensetracker)
        u_text_field=Builder.load_string(u_textField)
        p_text_field=Builder.load_string(p_textField)
        loginButton=Builder.load_string(l_button)
        s_Label=Builder.load_string(signupLabel)
        s_Label=Builder.load_string(signupLabel)
        screen.add_widget(E_Tracker,u_text_field,p_text_field)
        screen.add_widget(loginButton,s_Label)
        return screen