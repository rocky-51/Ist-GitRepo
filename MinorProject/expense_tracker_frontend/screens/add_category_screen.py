add_category_screen = """
<AddCategoryScreen>:
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
            padding: "25dp"
            spacing: "15dp"

            MDTopAppBar:
                title: "Add Category"
                elevation: 10

            MDTextField:
                id: name
                hint_text: "Category Name"
                icon_right: "shape"

            MDTextField:
                id: color
                hint_text: "Category Color (e.g. #FF5733)"
                helper_text: "Enter hex color code or name (optional)"
                helper_text_mode: "on_focus"
                icon_right: "palette"

            MDRoundFlatButton :
                text: "Add Category"
                on_release: root.add_category()

            MDRoundFlatButton :
                text: "Back to Dashboard"
                on_release: root.manager.current = "dashboard"
"""