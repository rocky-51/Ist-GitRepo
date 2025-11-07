home_screen='''
<HomeScreen>:
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        MDTopAppBar:
            title: "My Transactions"
            elevation: 10

        ScrollView:
            MDList:
                id: transactions_list

        MDFloatingActionButton:
            icon: "plus"
            pos_hint: {"center_x": 0.9, "center_y": 0.1}
            md_bg_color: app.theme_cls.primary_color
            on_release: root.manager.current = "add_transaction"
'''