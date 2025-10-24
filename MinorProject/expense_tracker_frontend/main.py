import requests
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen

BASE_URL = "http://127.0.0.1:8000/api/"

KV = """
ScreenManager:
    LoginScreen:
    RegisterScreen:
    DashboardScreen:
    AddExpenseScreen:
    HistoryScreen:

<LoginScreen>:
    name: "login"
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(40)
        MDLabel:
            text: "Expenses Tracker"
            halign: "center"
            font_style: "H4"
        MDTextField:
            id: username
            hint_text: "Username"
            icon_right: "account"
        MDTextField:
            id: password
            hint_text: "Password"
            icon_right: "key"
            password: True
        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": 0.5}
            on_release:
                app.login(username.text, password.text)
        MDRaisedButton:
            text: "Register"
            pos_hint: {"center_x": 0.5}
            on_release:
                root.manager.current = "register"

<RegisterScreen>:
    name: "register"
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(40)
        MDLabel:
            text: "Register"
            halign: "center"
            font_style: "H4"
        MDTextField:
            id: reg_username
            hint_text: "Username"
            icon_right: "account"
        MDTextField:
            id: reg_password
            hint_text: "Password"
            icon_right: "key"
            password: True
        MDTextField:
            id: reg_password2
            hint_text: "Confirm Password"
            icon_right: "key"
            password: True
        MDRaisedButton:
            text: "Register"
            pos_hint: {"center_x": 0.5}
            on_release:
                app.register(reg_username.text, reg_password.text, reg_password2.text)
        MDRaisedButton:
            text: "Back to Login"
            pos_hint: {"center_x": 0.5}
            on_release:
                root.manager.current = "login"

<DashboardScreen>:
    name: "dashboard"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            text: "Dashboard"
            halign: "center"
            font_style: "H4"
        MDRaisedButton:
            text: "Add Expense"
            on_release:
                root.manager.current = "add_expense"
        MDRaisedButton:
            text: "View History"
            on_release:
                root.manager.current = "history"
        MDLabel:
            id: total_label
            text: "Total Expenses: $0"
            halign: "center"
        MDRaisedButton:
            text: "Logout"
            on_release:
                root.manager.current = "login"

<AddExpenseScreen>:
    name: "add_expense"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)
        MDTextField:
            id: name
            hint_text: "Expense Name"
        MDTextField:
            id: amount
            hint_text: "Amount"
            input_filter: "float"
        MDRaisedButton:
            text: "Add"
            pos_hint: {"center_x": 0.5}
            on_release:
                app.add_expense(name.text, amount.text)
        MDRaisedButton:
            text: "Back"
            pos_hint: {"center_x": 0.5}
            on_release:
                root.manager.current = "dashboard"

<HistoryScreen>:
    name: "history"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Expense History"
            font_style: "H4"
            halign: "center"
        ScrollView:
            MDList:
                id: expense_list
        MDRaisedButton:
            text: "Back"
            pos_hint: {"center_x": 0.5}
            on_release:
                root.manager.current = "dashboard"
"""

class LoginScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    pass

class DashboardScreen(MDScreen):
    pass

class AddExpenseScreen(MDScreen):
    pass

class HistoryScreen(MDScreen):
    pass

class ExpensesApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.sm = Builder.load_string(KV)
        self.token = None
        self.expenses = []
        self.dialog = None
        return self.sm

    # --- Dialog helper ---
    def show_dialog(self, title, text):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(title=title, text=text, size_hint=(0.8, None), height=200)
        self.dialog.open()

    # --- Login ---
    def login(self, username, password):
        if not username or not password:
            self.show_dialog("Error", "Please enter username and password")
            return
        url = BASE_URL + "login/"
        try:
            response = requests.post(url, data={"username": username, "password": password})
            if response.status_code == 200:
                self.token = response.json().get("token")
                self.sm.current = "dashboard"
                self.get_expenses()
            else:
                self.show_dialog("Login Failed", response.json().get("non_field_errors", "Invalid credentials"))
        except Exception as e:
            self.show_dialog("Error", str(e))

    # --- Register ---
    def register(self, username, password1, password2):
        if not username or not password1 or not password2:
            self.show_dialog("Error", "All fields are required")
            return
        if password1 != password2:
            self.show_dialog("Error", "Passwords do not match")
            return
        url = BASE_URL + "register/"
        try:
            response = requests.post(url, data={"username": username, "password": password1})
            if response.status_code == 201:
                self.show_dialog("Success", "Registration successful! Please login.")
                self.sm.current = "login"
            else:
                self.show_dialog("Registration Failed", str(response.json()))
        except Exception as e:
            self.show_dialog("Error", str(e))

    # --- Get Expenses ---
    def get_expenses(self):
        if not self.token:
            return
        url = BASE_URL + "expenses/"
        headers = {"Authorization": f"Token {self.token}"}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.expenses = response.json()
                self.update_total()
                self.update_history()
            else:
                self.show_dialog("Error", "Failed to fetch expenses")
        except Exception as e:
            self.show_dialog("Error", str(e))

    # --- Add Expense ---
    def add_expense(self, name, amount):
        if not name or not amount:
            self.show_dialog("Error", "Please enter expense name and amount")
            return
        url = BASE_URL + "expenses/"
        headers = {"Authorization": f"Token {self.token}"}
        try:
            data = {"transaction_name": name, "transaction_amount": amount}
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 201:
                self.get_expenses()
                self.sm.current = "dashboard"
            else:
                self.show_dialog("Error", "Failed to add expense")
        except Exception as e:
            self.show_dialog("Error", str(e))

    # --- Update UI ---
    def update_total(self):
        total = sum(float(exp['transaction_amount']) for exp in self.expenses)
        self.sm.get_screen("dashboard").ids.total_label.text = f"Total Expenses: ${total:.2f}"

    def update_history(self):
        expense_list = self.sm.get_screen("history").ids.expense_list
        expense_list.clear_widgets()
        for exp in self.expenses:
            expense_list.add_widget(OneLineListItem(text=f"{exp['transaction_name']} - ${exp['transaction_amount']}"))

ExpensesApp().run()
