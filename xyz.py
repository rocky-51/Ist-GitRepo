from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(300,500)

screen_helper="""
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDTopAppBar:
                        title:'Dashboard'
                        left_action_items:[["menu",lambda x: nav_drawer.set_state("open")]]
                        elevation:8
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "Database Schema.png"

                MDLabel:
                    text: "Attreya"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "attreya01@gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Profile"
                            IconLeftWidget:
                                icon: "account"
                        OneLineIconListItem:
                            text: "Upload"
                            IconLeftWidget:
                                icon: "upload"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"

"""

# MDLabel:
#                         text:'Enter:'
#                         halign:'center'
#                     MDBottomAppBar:
#                         MDTopAppBar:
#                             left_action_items:[["coffee",lambda x:app.navigation_draw()]]
#                             mode:'end'
#                             type:'bottom'
#                             on_action_button:app.navigation_draw()

class xyz(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        screen=Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")

xyz().run()