change_password_screen='''
<ChangePasswordScreen>:
    name: "change_password"

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"

        MDTopAppBar:
            title: "Change Password"
            left_action_items: [["arrow-left", lambda x: root.load_dashboard()]]

        MDTextField:
            id: current_password
            hint_text: "Current Password"
            password: True
            mode: "rectangle"

        MDTextField:
            id: new_password
            hint_text: "New Password"
            password: True
            mode: "rectangle"
        
        MDTextField:
            id: confirm_password
            hint_text: "Confirm New Password"
            password: True
            mode: "rectangle"

        MDRaisedButton:
            text: "Update Password"
            md_bg_color: 0, 0.6, 1, 1
            on_release: root.change_password()
'''