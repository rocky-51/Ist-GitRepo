from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivy.lang import Builder
from screens.helper import expensetracker
from screens.register_screen import register_screen
# from screens.home_screen import home_screen
from screens.dashboard_screen import dashboard_screen
from screens.add_category_screen import add_category_screen
from screens.add_transaction_screen import add_transaction_screen
from screens.update_transaction_screen import update_transaction_screen
import requests
import json
import os

TOKEN_FILE = "auth_token.json"


class ExpenseTrackerApp(MDApp):
    API_BASE = "http://127.0.0.1:8000/api"
    TOKEN_URL = f"{API_BASE}/token/"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        # Load screens
        Builder.load_string(expensetracker)
        Builder.load_string(register_screen)
        Builder.load_string(dashboard_screen)
        # Builder.load_string(home_screen)
        # Builder.load_file("screens/home_screen.kv")
        Builder.load_string(add_category_screen)
        Builder.load_string(add_transaction_screen)
        # Builder.load_string(update_transaction_screen)

        sm = MDScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(AddCategoryScreen(name="add_category"))
        sm.add_widget(AddTransactionScreen(name="add_transaction"))
        sm.add_widget(UpdateTransactionScreen(name="update_transaction"))
        return sm


# --------------------- HOME ---------------------
# --------------------- HOME (Transaction List & Edit) ---------------------
class HomeScreen(MDScreen):
    def on_enter(self):
        self.load_transactions()

    def get_headers(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                data = json.load(f)
                access = data.get("access")
                return {"Authorization": f"Bearer {access}"}
        return {}

    def load_transactions(self):
        app = MDApp.get_running_app()
        headers = self.get_headers()

        try:
            response = requests.get(f"{app.API_BASE}/transactions/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                self.ids.transactions_list.clear_widgets()
                from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget

                for t in data[::-1]:
                    item = TwoLineIconListItem(
                        text=f"{t['transaction_name']} - ₹{t['transaction_amount']}",
                        secondary_text=f"{t['transaction_date']} {t['transaction_time']}",
                        on_release=lambda x, tid=t['transaction_id']: self.edit_transaction(tid),
                    )
                    item.add_widget(IconLeftWidget(icon="pencil"))
                    self.ids.transactions_list.add_widget(item)
            else:
                toast("No transactions found.")
        except Exception as e:
            toast(f"Error: {e}")

    def edit_transaction(self, transaction_id):
        # Store ID temporarily and move to Update Screen
        app = MDApp.get_running_app()
        app.transaction_to_edit = transaction_id
        self.manager.current = "update_transaction"


# --------------------- UPDATE TRANSACTION ---------------------
class UpdateTransactionScreen(MDScreen):
    def on_pre_enter(self):
        """Load existing transaction details."""
        app = MDApp.get_running_app()
        tid = getattr(app, "transaction_to_edit", None)
        if not tid:
            toast("No transaction selected.")
            self.manager.current = "home"
            return

        headers = DashboardScreen().get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/transactions/{tid}/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                self.ids.name.text = data["transaction_name"]
                self.ids.amount.text = str(data["transaction_amount"])
                self.ids.category.text = str(data["category"])
            else:
                toast("Could not fetch transaction details.")
        except Exception as e:
            toast(f"Error: {e}")

    def update_transaction(self):
        """Send updated data to backend."""
        app = MDApp.get_running_app()
        tid = getattr(app, "transaction_to_edit", None)
        headers = DashboardScreen().get_headers()

        name = self.ids.name.text.strip()
        amount = self.ids.amount.text.strip()
        category = self.ids.category.text.strip()

        if not name or not amount or not category:
            toast("Please fill all fields")
            return

        data = {
            "transaction_name": name,
            "transaction_amount": amount,
            "category": category,
        }

        try:
            response = requests.put(
                f"{app.API_BASE}/transactions/{tid}/",
                data=data,
                headers=headers,
            )
            if response.status_code in (200, 202):
                toast("Transaction updated successfully!")
                self.manager.current = "home"
            else:
                toast("Failed to update transaction.")
        except Exception as e:
            toast(f"Error: {e}")

# --------------------- LOGIN ---------------------
class LoginScreen(MDScreen):
    def login(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        if not email or not password:
            toast("Enter both email and password")
            return

        try:
            response = requests.post(
                ExpenseTrackerApp.TOKEN_URL,
                data={"email": email, "password": password},
            )
            if response.status_code == 200:
                token_data = response.json()
                with open(TOKEN_FILE, "w") as f:
                    json.dump(token_data, f)
                toast("Login successful!")
                self.manager.current = "dashboard"
            else:
                toast("Invalid credentials — please register first.")
                self.manager.current = "register"
        except Exception as e:
            toast(f"Error: {e}")


# --------------------- REGISTER ---------------------
class RegisterScreen(MDScreen):
    def register_user(self):
        name = self.ids.name.text.strip()
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        if not name or not email or not password:
            toast("Please fill all fields")
            return

        try:
            response = requests.post(
                f"{ExpenseTrackerApp.API_BASE}/users/",
                data={"name": name, "email": email, "password": password},
            )
            if response.status_code in (200, 201):
                toast("Registration successful! Please log in.")
                self.manager.current = "login"
            else:
                toast("Registration failed.")
        except Exception as e:
            toast(f"Error: {e}")


# --------------------- DASHBOARD ---------------------
class DashboardScreen(MDScreen):
    def on_enter(self):
        self.load_dashboard()

    def get_headers(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                data = json.load(f)
                access = data.get("access")
                return {"Authorization": f"Bearer {access}"}
        return {}

    def load_dashboard(self):
        app = MDApp.get_running_app()
        headers = self.get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/transactions/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                total_expenses = sum(float(t["transaction_amount"]) for t in data)
                self.ids.balance.text = f"₹{10000 - total_expenses:.2f}"
                self.ids.expenses.text = f"₹{total_expenses:.2f}"

                self.ids.transactions_list.clear_widgets()
                from kivymd.uix.list import OneLineListItem
                for t in data[-5:][::-1]:
                    self.ids.transactions_list.add_widget(
                        OneLineListItem(
                            text=f"{t['transaction_name']} - ₹{t['transaction_amount']}"
                        )
                    )
            else:
                toast("No transactions found.")
        except Exception as e:
            toast(f"Error: {e}")

    def logout(self):
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
        toast("Logged out successfully")
        self.manager.current = "home"


# --------------------- ADD CATEGORY ---------------------
class AddCategoryScreen(MDScreen):
    def add_category(self):
        app = MDApp.get_running_app()
        name = self.ids.name.text.strip()
        color = self.ids.color.text.strip()

        if not name:
            toast("Please enter a category name")
            return

        headers = DashboardScreen().get_headers()
        data = {"category_name": name}
        if color:
            data["category_color"] = color

        try:
            response = requests.post(
                f"{app.API_BASE}/categories/",
                data=data,
                headers=headers,
            )
            if response.status_code in (200, 201):
                toast("Category added successfully!")
                self.ids.name.text = ""
                self.ids.color.text = ""
                self.manager.current = "dashboard"
            else:
                toast("Failed to add category.")
        except Exception as e:
            toast(f"Error: {e}")


# --------------------- ADD TRANSACTION ---------------------
class AddTransactionScreen(MDScreen):
    def add_transaction(self):
        app = MDApp.get_running_app()
        name = self.ids.name.text.strip()
        amount = self.ids.amount.text.strip()
        category = self.ids.category.text.strip()
        date = self.ids.date.text.strip()
        time = self.ids.time.text.strip()

        if not name or not amount or not category:
            toast("Please fill required fields")
            return

        headers = DashboardScreen().get_headers()
        data = {
            "transaction_name": name,
            "transaction_amount": amount,
            "category": category,
        }
        if date:
            data["transaction_date"] = date
        if time:
            data["transaction_time"] = time

        try:
            response = requests.post(
                f"{app.API_BASE}/transactions/",
                data=data,
                headers=headers,
            )
            if response.status_code == 201:
                toast("Transaction added successfully!")
                self.manager.current = "dashboard"
            else:
                toast("Failed to add transaction.")
        except Exception as e:
            toast(f"Error: {e}")


if __name__ == "__main__":
    ExpenseTrackerApp().run()
