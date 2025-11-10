dashboard_screen='''
<DashboardScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "20dp"

        MDTopAppBar:
            title: "Dashboard"
            right_action_items: [["logout", lambda x: root.logout()]]

        MDLabel:
            text: "Total Balance"
            halign: "center"
        MDLabel:
            id: balance
            text: "₹0.00"
            halign: "center"
            font_style: "H5"

        MDLabel:
            text: "Expenses"
            halign: "center"
        MDLabel:
            id: expenses
            text: "₹0.00"
            halign: "center"
            font_style: "H6"

        MDLabel:
            text: "Recent Transactions"
            halign: "left"
            font_style: "H6"

        ScrollView:
            MDList:
                id: transactions_list

        # Floating buttons
        MDFloatingActionButton:
            icon: "shape-plus"
            pos_hint: {"center_x": 0.8, "center_y": 0.1}
            on_release: root.manager.current = "add_category"

        MDFloatingActionButton:
            icon: "plus"
            pos_hint: {"center_x": 0.95, "center_y": 0.1}
            on_release: root.manager.current = "add_transaction"
            
        MDFloatingActionButton:
            icon: "file-document"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": 0.65, "center_y": 0.1}
            on_release: root.manager.current = "transactions"

'''