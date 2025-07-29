from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton

class SimpleApp(MDApp):
    
    def build(self):
        screen = Screen()
        label = MDLabel(
            text="Welcome to KivyMD!",
            halign="center",
            font_style="H5"
        )
        icon_Label=MDIcon(text='library-video',halign='center')
        btn_flt=MDRectangleFlatButton(text='Hello World',pos_hint={'center_x':0.5,'center_y':0.5})
        icon_btn=MDFloatingActionButton(icon='language-python',pos_hint={'center_x':0.5,'center_y':0.5})
        screen.add_widget(icon_btn)
        return screen
SimpleApp().run()
