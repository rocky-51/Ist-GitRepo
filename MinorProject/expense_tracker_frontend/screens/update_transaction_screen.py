update_transaction_screen = '''
<UpdateTransactionScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: "25dp"
        spacing: "15dp"

        MDTopAppBar:
            title: "Update Transaction"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: root.manager.current = "home"]]

        MDTextField:
            id: name
            hint_text: "Transaction Name"
            icon_right: "note-edit"

        MDTextField:
            id: amount
            hint_text: "Amount (₹)"
            input_filter: "float"
            icon_right: "cash"

        MDTextField:
            id: category
            hint_text: "Category ID"
            helper_text: "Enter the updated category ID"
            helper_text_mode: "on_focus"
            icon_right: "shape"

        MDRaisedButton:
            text: "Save Changes"
            md_bg_color: 0, 1, 1, 1
            on_release: root.update_transaction()
'''