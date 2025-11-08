add_category_screen = """
<AddCategoryScreen>:
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

        MDRaisedButton:
            text: "Add Category"
            md_bg_color: 0, 1, 1, 1
            on_release: root.add_category()

        MDTextButton:
            text: "← Back to Dashboard"
            on_release: root.manager.current = "dashboard"
            pos_hint: {"center_x": 0.5}
"""