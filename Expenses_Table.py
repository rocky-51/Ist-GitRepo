from kivymd.app import MDApp    
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
Window.size=(300,500)
# from kivy.config import Config
# Config.set('graphics', 'width', '700')  # Set width to 800 pixels
# Config.set('graphics', 'height', '350')

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
                                    ],
                          row_data=[
                                        ("101","1001","Expenditure","Black"),
                                        ("102","1002","Buying","Blue"),
                                        ("103","1003","Fruits","Yellow"),
                                        ("104","1004","Vegetables","Green")
                                    ]       
                        )
        screen.add_widget(table)
        return screen

Expenses_Table().run()