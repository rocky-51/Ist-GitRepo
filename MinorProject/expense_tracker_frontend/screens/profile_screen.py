profile_screen='''
<ProfileScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "15dp"

        MDTopAppBar:
            title: "Profile"
            left_action_items: [["arrow-left", lambda x: root.load_dashboard()]]

        MDTextField:
            id: user_name
            hint_text: "Your Name"
            mode: "rectangle"

        MDTextField:
            id: user_email
            hint_text: "Your Email"
            mode: "rectangle"
            readonly: True  # Email usually not editable

        MDRaisedButton:
            text: "Update Profile"
            md_bg_color: 0, 0.6, 1, 1
            on_release: root.update_profile()

        MDRaisedButton:
            text: "Delete Account"
            md_bg_color: 1, 0, 0, 1
            on_release: root.delete_account()
        
        MDRaisedButton:
            text: "Change Password"
            md_bg_color: 0,0.6,1,1
            on_release: root.manager.current = "change_password"
'''