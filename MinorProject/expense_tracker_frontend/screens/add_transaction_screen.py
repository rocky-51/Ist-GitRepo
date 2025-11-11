add_transaction_screen='''
<AddTransactionScreen>:
    MDCard :
        size_hint : None,None
        size : 1000,800
        pos_hint : {"center_x":.5,"center_y":.5}
        elevation : 15
        md_bg_color : [50/255,50/255,50/255,1]
        padding : 10
        spacing : 20
        orientation : "vertical"
        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "10dp"

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

            MDRoundFlatButton :
                text: "Add Transaction"
                on_release: root.add_transaction()

            MDRoundFlatButton :
                text: "Back to Dashboard"
                on_release: root.manager.current = "dashboard"
'''