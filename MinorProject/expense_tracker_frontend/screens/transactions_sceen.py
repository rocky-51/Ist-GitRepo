transactions_screen='''
<TransactionsScreen>:
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
