dashboard_screen='''
<DashboardScreen>:
    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "20dp"

        MDTopAppBar:
            title: "Dashboard"
            elevation: 10
            right_action_items: [["logout", lambda x: root.logout()]]

        # Balance Summary
        MDBoxLayout:
            orientation: "horizontal"
            spacing: "15dp"
            size_hint_y: None
            height: "120dp"

            MDCard:
                orientation: "vertical"
                size_hint: 0.5, 1
                md_bg_color: (0, 0.5, 0.5, 1)
                radius: [20, 20, 20, 20]
                padding: "10dp"
                MDLabel:
                    text: "Total Balance"
                    theme_text_color: "Custom"
                    text_color: (1, 1, 1, 1)
                MDLabel:
                    id: balance
                    text: "₹0.00"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: (1, 1, 1, 1)
                    font_style: "H5"

            MDCard:
                orientation: "vertical"
                size_hint: 0.5, 1
                md_bg_color: (0.2, 0.2, 0.2, 1)
                radius: [20, 20, 20, 20]
                padding: "10dp"
                MDLabel:
                    text: "Expenses"
                    theme_text_color: "Custom"
                    text_color: (1, 0.4, 0.4, 1)
                MDLabel:
                    id: expenses
                    text: "₹0.00"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: (1, 0.4, 0.4, 1)
                    font_style: "H5"

        MDLabel:
            text: "Recent Transactions"
            halign: "left"
            font_style: "H6"
            padding: [10, 10]

        ScrollView:
            MDList:
                id: transactions_list

        MDFloatingActionButton:
            icon: "plus"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": 0.9, "center_y": 0.1}
            on_release: root.manager.current = "add_transaction"
        
        MDFloatingActionButton:
            icon: "shape-plus"
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": 0.8, "center_y": 0.1}
            on_release: root.manager.current = "add_category"
'''