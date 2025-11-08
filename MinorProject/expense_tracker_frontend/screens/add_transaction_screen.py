add_transaction_screen='''
<AddTransactionScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: "25dp"
        spacing: "15dp"

        MDTopAppBar:
            title: "Add Transaction"
            elevation: 10
            # left_action_items: [['arrow-left', 'on_release', app.root.current = 'dashboard']]

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
            helper_text: "Enter numeric category ID (e.g. 1 for Food)"
            helper_text_mode: "on_focus"
            icon_right: "shape"

        MDTextField:
            id: date
            hint_text: "Date (YYYY-MM-DD)"
            helper_text: "Leave empty for today"
            icon_right: "calendar"

        MDTextField:
            id: time
            hint_text: "Time (HH:MM:SS)"
            helper_text: "Leave empty for current time"
            icon_right: "clock"

        MDRaisedButton:
            text: "Add Transaction"
            md_bg_color: 0, 1, 1, 1
            on_release: root.add_transaction()

        MDTextButton:
            text: "← Back to Dashboard"
            on_release: root.manager.current = "dashboard"
'''