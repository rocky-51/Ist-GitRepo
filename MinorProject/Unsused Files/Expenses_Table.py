from kivymd.app import MDApp    
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
Window.size=(300,500)


class Expenses_Table(MDApp):
    def build(self):
        screen=Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        table=MDDataTable(pos_hint={'center_x':0.5,'center_y':0.5},
                          size_hint=(0.9,0.6),
                          column_data=[
                                        ("Category_ID",dp(30)),
                                        ("User_ID",dp(30)),
                                        ("Category_Name",dp(30)),
                                        ("Category_Color",dp(30))
                                    ]      
                        )
        screen.add_widget(table)
        return screen

Expenses_Table().run()