register_screen='''
<RegisterScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "40dp"

        MDLabel:
            text: "Create Account"
            halign: "center"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 0, 1, 1, 1

        MDTextField:
            id: name
            hint_text: "Full Name"
            icon_right: "account"

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
            text: "Register"
            md_bg_color: 0, 1, 1, 1
            on_release: root.register_user()

        MDTextButton:
            text: "← Back to Login"
            on_release: root.manager.current = "login"
'''