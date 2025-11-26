splash_screen='''
<SplashScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "40dp"
        md_bg_color: 0, 0.2, 0.25, 1  # calm teal background
        opacity: 1

        Widget:  # spacer

        Image:
            id: logo
            source: "assets/logo.png"  # <-- replace with your image path
            size_hint: None, None
            size: "140dp", "140dp"
            pos_hint: {"center_x": 0.5}
            opacity: 0  # start invisible

        MDLabel:
            id: app_name
            text: "X-Track"
            halign: "center"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            opacity: 0  # start invisible

        MDLabel:
            text: "Track. Save. Grow."
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0.8, 0.9, 0.9, 1

        Widget:  # spacer

        MDSpinner:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {"center_x": 0.5}
            active: True
'''