edit_transaction_screen="""
<EditTransactionScreen>:
    name: "edit_transaction"

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "15dp"

        MDTopAppBar:
            title: "Edit Transaction"
            left_action_items: [["arrow-left", lambda x: root.go_back_to_transactions()]]

        MDTextField:
            id: edit_name
            hint_text: "Transaction Name"

        MDTextField:
            id: edit_amount
            hint_text: "Amount"
            input_filter: "float"

        MDTextField:
            id: edit_date
            hint_text: "Date (YYYY-MM-DD)"

        MDTextField:
            id: edit_time
            hint_text: "Time (HH:MM:SS)"

        MDRaisedButton:
            text: "Save Changes"
            md_bg_color: 0, 0.7, 1, 1
            on_release: root.update_transaction()
"""