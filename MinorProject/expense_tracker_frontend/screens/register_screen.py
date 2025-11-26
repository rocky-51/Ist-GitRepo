register_screen='''
<RegisterScreen>:
    MDCard :
        size_hint : None,None
        size : 800,700
        pos_hint : {"center_x":.5,"center_y":.5}
        elevation : 15
        md_bg_color : [50/255,50/255,50/255,1]
        padding : 20
        spacing : 30
        orientation : "vertical"
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

            MDRoundFlatButton :
                text: "Register"
                on_release: root.register_user()

            MDRoundFlatButton :
                text: "Back to Login"
                on_release: root.manager.current = "login"
'''