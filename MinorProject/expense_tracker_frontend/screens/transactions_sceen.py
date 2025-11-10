transactions_screen='''
<TransactionsScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: "15dp"
        spacing: "10dp"

        MDTopAppBar:
            title: "My Transactions"
            left_action_items: [["arrow-left", lambda x: root.load_dashboard()]]
            right_action_items: [["logout", lambda x: root.logout()]]


        ScrollView:
            MDList:
                id: transactions_list

        MDFloatingActionButton:
            icon: "refresh"
            pos_hint: {"center_x": 0.9, "center_y": 0.1}
            on_release: root.load_transactions()

'''
