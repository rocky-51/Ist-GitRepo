login_screen='''
<LoginScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "40dp"
        MDLabel:
            text: "Expense Tracker"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 1, 1, 1
            font_style: "H4"

        MDTextField:
            id: email
            hint_text: "Email"
            icon_right: "email"
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            icon_right: "lock"

        MDRaisedButton:
            text: "Login"
            md_bg_color: 0, 1, 1, 1
            on_release: root.login()
'''
