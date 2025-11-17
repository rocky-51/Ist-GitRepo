add_transaction_screen='''
<AddTransactionScreen>:
    MDCard:
        size_hint: None, None
        size: 1000, 800
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 15
        md_bg_color: [50/255, 50/255, 50/255, 1]
        padding: 20
        orientation: "vertical"

        MDBoxLayout:
            orientation: "vertical"
            spacing: "20dp"
            padding: "20dp"

            MDTopAppBar:
                title: "Add Transaction"
                left_action_items: [["arrow-left", lambda x: root.load_dashboard()]]

            MDTextField:
                id: transaction_name
                hint_text: "Transaction Name"
                icon_right: "note-edit"
                mode: "rectangle"

            MDTextField:
                id: transaction_amount
                hint_text: "Amount (₹)"
                input_filter: "float"
                icon_right: "currency-inr"
                mode: "rectangle"

            MDTextField:
                id: category_name
                hint_text: "Select Category"
                readonly: True
                mode: "rectangle"
                on_focus:
                    if self.focus: root.open_category_menu()

            MDTextField:
                id: transaction_date
                hint_text: "Date (YYYY-MM-DD)"
                mode: "rectangle"

            MDTextField:
                id: transaction_time
                hint_text: "Time (HH:MM:SS)"
                mode: "rectangle"

            MDRaisedButton:
                text: "Add Transaction"
                md_bg_color: 0, 0.7, 1, 1
                on_release: root.add_transaction()

'''