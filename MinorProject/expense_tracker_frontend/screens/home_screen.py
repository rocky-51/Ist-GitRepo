home_screen='''
<HomeScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "30dp"
        padding: "40dp"
        MDLabel:
            text: "💰 Expense Tracker"
            halign: "center"
            font_style: "H4"

        MDLabel:
            text: "Track your spending smartly"
            halign: "center"

        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "login"

        MDFlatButton:
            text: "Register"
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "register"
'''