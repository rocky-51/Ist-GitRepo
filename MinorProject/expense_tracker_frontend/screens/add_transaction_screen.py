add_transaction_screen='''
<AddTransactionScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: "30dp"
        spacing: "20dp"

        MDLabel:
            text: "Add Transaction"
            halign: "center"
            font_style: "H5"

        MDTextField:
            id: name
            hint_text: "Transaction Name"
        MDTextField:
            id: amount
            hint_text: "Amount"
            input_filter: "float"
        MDTextField:
            id: category
            hint_text: "Category ID"

        MDRaisedButton:
            text: "Save"
            md_bg_color: 0, 1, 1, 1
            on_release: root.add_transaction()

        MDTextButton:
            text: "← Back"
            on_release: root.manager.current = "home"
'''