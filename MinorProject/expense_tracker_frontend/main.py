from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.toast import toast
from kivymd.uix.list import OneLineListItem
from kivy.lang import Builder
# from screens.login_screen import login_screen
from screens.helper import expensetracker
from screens.register_screen import register_screen
from screens.dashboard_screen import dashboard_screen
from screens.add_category_screen import add_category_screen
from screens.add_transaction_screen import add_transaction_screen
import requests
import json
import os

# Load screen layouts
# Builder.load_string(login_screen)
Builder.load_string(expensetracker)
Builder.load_string(register_screen)
Builder.load_string(dashboard_screen)
Builder.load_string(add_category_screen)
Builder.load_string(add_transaction_screen)

TOKEN_FILE = "auth_token.json"


class ExpenseTrackerApp(MDApp):
    API_BASE = "http://127.0.0.1:8000/api"
    TOKEN_URL = "http://127.0.0.1:8000/api/token/"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        self.sm = MDScreenManager()
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegisterScreen(name="register"))
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(DashboardScreen(name="dashboard"))
        self.sm.add_widget(AddCategoryScreen(name="add_category"))
        self.sm.add_widget(AddTransactionScreen(name="add_transaction"))
        return self.sm

    def save_token(self, token_data):
        """Save token to local file"""
        with open(TOKEN_FILE, "w") as f:
            json.dump(token_data, f)

    def load_token(self):
        """Load token from file if exists"""
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                return json.load(f)
        return None
    
    def refresh_token(self):
        token_data = self.load_token()
        if token_data and "refresh" in token_data:
            response = requests.post(
                f"{self.API_BASE}/token/refresh/",
                data={"refresh": token_data["refresh"]}
            )
            if response.status_code == 200:
                new_tokens = response.json()
                token_data.update(new_tokens)
                self.save_token(token_data)


    def get_headers(self):
        token_data = self.load_token()
        if token_data:
            access_token = token_data.get("access")
            return {"Authorization": f"Bearer {access_token}"}
        return {}


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
                app = MDApp.get_running_app()
                with open(TOKEN_FILE, "w") as f:
                    json.dump(token_data, f)
                toast("Login successful!")
                self.manager.current = "home"
            else:
                toast("Invalid credentials — please register first.")
                self.manager.current = "register"
        except Exception as e:
            toast(f"Error: {e}")


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
                data={
                    "name": name,
                    "email": email,
                    "password": password,
                },
            )

            if response.status_code in (200, 201):
                toast("Registration successful! Please log in.")
                self.manager.current = "login"
            else:
                error = response.json()
                toast(f"Registration failed: {error}")
        except Exception as e:
            toast(f"Error: {e}")

class DashboardScreen(MDScreen):
    def on_enter(self):
        """Called when the dashboard is opened."""
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
                balance = 10000 - total_expenses  # Example logic

                self.ids.balance.text = f"₹{balance:,.2f}"
                self.ids.expenses.text = f"₹{total_expenses:,.2f}"

                self.ids.transactions_list.clear_widgets()
                for t in data[-5:][::-1]:  # last 5 transactions
                    self.ids.transactions_list.add_widget(
                        OneLineListItem(
                            text=f"{t['transaction_name']} - ₹{t['transaction_amount']}"
                        )
                    )
            else:
                toast("Failed to fetch dashboard data")
        except Exception as e:
            toast(f"Error: {e}")

    def logout(self):
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
        toast("Logged out successfully")
        self.manager.current = "login"

class HomeScreen(MDScreen):
    def on_enter(self):
        self.load_transactions()

    def load_transactions(self):
        app = MDApp.get_running_app()
        headers = app.get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/transactions/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                self.ids.transactions_list.clear_widgets()
                for t in data:
                    self.ids.transactions_list.add_widget(
                        OneLineListItem(text=f"{t['transaction_name']} - ₹{t['transaction_amount']}")
                    )
            else:
                toast("Unauthorized or failed to fetch transactions")
        except Exception as e:
            toast(f"Error: {e}")


class AddCategoryScreen(MDScreen):
    def add_category(self):
        app = MDApp.get_running_app()
        name = self.ids.name.text.strip()
        color = self.ids.color.text.strip()

        if not name:
            toast("Please enter a category name")
            return

        # JWT Token
        headers = {}
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                token_data = json.load(f)
                access = token_data.get("access")
                headers = {"Authorization": f"Bearer {access}"}

        # Payload
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
                try:
                    err = response.json()
                except:
                    err = response.text
                toast(f"Failed: {err}")
        except Exception as e:
            toast(f"Error: {e}")


class AddTransactionScreen(MDScreen):
    def add_transaction(self):
        app = MDApp.get_running_app()

        # Get user inputs
        name = self.ids.name.text.strip()
        amount = self.ids.amount.text.strip()
        category = self.ids.category.text.strip()
        date = self.ids.date.text.strip()
        time = self.ids.time.text.strip()

        # Validate fields
        if not name or not amount or not category:
            toast("Please fill at least name, amount, and category")
            return

        # Build request data
        data = {
            "transaction_name": name,
            "transaction_amount": amount,
            "category": category,
        }

        # Optional fields
        if date:
            data["transaction_date"] = date
        if time:
            data["transaction_time"] = time

        # Prepare headers (with JWT token)
        headers = {}
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                token_data = json.load(f)
                access = token_data.get("access")
                headers = {"Authorization": f"Bearer {access}"}

        # Send to backend
        try:
            response = requests.post(
                f"{app.API_BASE}/transactions/",
                data=data,
                headers=headers,
            )

            if response.status_code == 201:
                toast("Transaction added successfully!")
                # Clear inputs
                self.ids.name.text = ""
                self.ids.amount.text = ""
                self.ids.category.text = ""
                self.ids.date.text = ""
                self.ids.time.text = ""
                self.manager.current = "dashboard"
            else:
                try:
                    error = response.json()
                except:
                    error = response.text
                toast(f"Failed: {error}")
        except Exception as e:
            toast(f"Error: {e}")


if __name__ == "__main__":
    ExpenseTrackerApp().run()
