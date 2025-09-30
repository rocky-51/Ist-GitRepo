from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.app import MDApp 
requestsKV = """
BoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "My App"
        elevation: 4
        left_action_items: [["menu", lambda x: print("Menu clicked")]]

    ScrollView:
        MDList:
            id: expenses_list

    MDFloatingActionButton:
        icon: "plus"
        pos: "20dp", "20dp"
        md_bg_color: app.theme_cls.primary_color
        on_release: app.add_expense()
"""

class ExpenseApp(MDApp):
    API_URL = "http://127.0.0.1:8000/api/expenses/"

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(requestsKV)

    def on_start(self):
        self.load_expenses()

    def load_expenses(self):
        response = requestsKV.get(self.API_URL, headers={"Authorization": "Token your_api_token"})
        if response.status_code == 200:
            expenses = response.json()
            for exp in expenses:
                self.root.ids.expenses_list.add_widget(
                    self.create_expense_item(exp["title"], exp["amount"], exp["category"])
                )

    def create_expense_item(self, title, amount, category):
        from kivymd.uix.list import OneLineListItem
        return OneLineListItem(text=f"{title} - {category}: ₹{amount}")

    def add_expense(self):
        # Example: Add expense via POST
        data = {"title": "Tea", "category": "Food", "amount": "20.00"}
        requestsKV.post(self.API_URL, data=data, headers={"Authorization": "Token your_api_token"})
        self.root.ids.expenses_list.clear_widgets()
        self.load_expenses()

ExpenseApp().run()
