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
            pos_hint: {"center_x": 0.1}
        MDLabel:
            id: balance
            text: "₹0.00"
            halign: "center"
            font_style: "H6"
            pos_hint: {"center_x": 0.1}

        MDLabel:
            text: "Expenses"
            halign: "center"
            pos_hint: {"center_x": 0.1}
        MDLabel:
            id: expenses
            text: "₹0.00"
            halign: "center"
            font_style: "H6"
            pos_hint: {"center_x": 0.1}

        ScrollView:
            MDList:
                id: transactions_list

        # Floating buttons
        MDRaisedButton:
            icon: "shape-plus"
            text: "Add Category"
            pos_hint: {"center_x": 0.95, "center_y": 0.1}
            on_release: root.manager.current = "add_category"

        MDRaisedButton:
            icon: "plus"
            text: "Add Transaction"
            pos_hint: {"center_x": 0.95, "center_y": 0.1}
            on_release: root.manager.current = "add_transaction"
            
        MDRaisedButton:
            icon: "file-document"
            text: "Transactions"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": 0.95, "center_y": 0.1}
            on_release: root.manager.current = "transactions"
        
        MDRaisedButton:
            icon: "account"
            text: "Profile"
            pos_hint: {"center_x": 0.95, "center_y": 0.1}
            on_release: app.root.current = "profile"
'''