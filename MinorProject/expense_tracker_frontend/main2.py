from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.toast import toast
from kivy.lang import Builder
from screens.splash_screen import splash_screen
from screens.helper import expensetracker
from screens.register_screen import register_screen
from screens.dashboard_screen import dashboard_screen
from screens.add_category_screen import add_category_screen
from screens.add_transaction_screen import add_transaction_screen
from screens.transactions_sceen import transactions_screen
from kivy.uix.screenmanager import FadeTransition
from kivy.clock import Clock
from kivy.animation import Animation

import requests
import json
import os

TOKEN_FILE = "auth_token.json"

DEFAULT_CATEGORIES = [
    {"text": "Food & Dining", "color": "#E57373"},
    {"text": "Transportation", "color": "#64B5F6"},
    {"text": "Shopping", "color": "#BA68C8"},
    {"text": "Entertainment", "color": "#FFD54F"},
    {"text": "Bills & Utilities", "color": "#81C784"},
    {"text": "Healthcare", "color": "#4DB6AC"},
    {"text": "Education", "color": "#A1887F"},
    {"text": "Groceries", "color": "#FFF176"},
    {"text": "Travel", "color": "#7986CB"},
    {"text": "Miscellaneous", "color": "#B0BEC5"},
]


class ExpenseTrackerApp(MDApp):
    API_BASE = "http://127.0.0.1:8000/api"
    TOKEN_URL = f"{API_BASE}/token/"
    
    def get_headers(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                data = json.load(f)
                access = data.get("access")
                return {"Authorization": f"Bearer {access}"}
        return {}

    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"

        # Load screens
        Builder.load_string(splash_screen)
        Builder.load_string(expensetracker)
        Builder.load_string(register_screen)
        Builder.load_string(dashboard_screen)
        Builder.load_string(add_category_screen)
        Builder.load_string(add_transaction_screen)
        Builder.load_string(transactions_screen)


        sm = MDScreenManager(transition=FadeTransition(duration=0.5)) 
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(AddCategoryScreen(name="add_category"))
        sm.add_widget(AddTransactionScreen(name="add_transaction"))
        sm.add_widget(TransactionsScreen(name="transactions"))
        sm.current = "splash"
        return sm

# --------------------- SPLASH SCREEN ---------------------

class SplashScreen(MDScreen):
    def on_enter(self):
        # Start fade-in animation for logo and text
        self.ids.logo.opacity = 0
        self.ids.app_name.opacity = 0

        fade_in = Animation(opacity=1, duration=1.5)
        fade_in.start(self.ids.logo)
        fade_in.start(self.ids.app_name)

        # After fade-in, stay for a while, then fade-out
        Clock.schedule_once(self.start_fade_out, 5)

    def start_fade_out(self, *args):
        fade_out = Animation(opacity=0, duration=1)
        fade_out.bind(on_complete=lambda *x: self.go_to_login())
        fade_out.start(self)

    def go_to_login(self, *args):
        self.manager.current = "login"
        self.opacity = 1  # reset opacity for next time

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

    def load_dashboard(self):
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()
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
        self.manager.current = "login"

# --------------------- TRANSACTIONS SCREEN ---------------------
class TransactionsScreen(MDScreen):
    def on_enter(self):
        headers = MDApp.get_running_app().get_headers()

    def get_headers(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                data = json.load(f)
                access = data.get("access")
                return {"Authorization": f"Bearer {access}"}
        return {}

    def load_transactions(self):
        """Fetch all transactions from backend"""
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()

        try:
            response = requests.get(f"{app.API_BASE}/transactions/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                self.ids.transactions_list.clear_widgets()
                from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget, IconRightWidget

                for t in data[::-1]:  # newest first
                    item = TwoLineIconListItem(
                        text=f"{t['transaction_name']} - ₹{t['transaction_amount']}",
                        secondary_text=f"{t['transaction_date']} | Category: {t['category']}",
                    )

                    # Edit icon
                    edit_icon = IconLeftWidget(
                        icon="pencil",
                        on_release=lambda x, tid=t["transaction_id"]: self.edit_transaction(tid),
                    )
                    item.add_widget(edit_icon)

                    # Delete icon
                    delete_icon = IconRightWidget(
                        icon="delete",
                        on_release=lambda x, tid=t["transaction_id"]: self.delete_transaction(tid),
                    )
                    item.add_widget(delete_icon)

                    self.ids.transactions_list.add_widget(item)
            else:
                toast("No transactions found.")
        except Exception as e:
            toast(f"Error: {e}")

    def edit_transaction(self, transaction_id):
        """Store selected transaction ID and move to Update Screen"""
        app = MDApp.get_running_app()
        app.transaction_to_edit = transaction_id
        self.manager.current = "update_transaction"

    def delete_transaction(self, transaction_id):
        """Delete selected transaction"""
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()

        try:
            response = requests.delete(
                f"{app.API_BASE}/transactions/{transaction_id}/", headers=headers
            )
            if response.status_code in (200, 204):
                toast("Transaction deleted successfully.")
                self.load_transactions()
            else:
                toast("Failed to delete transaction.")
        except Exception as e:
            toast(f"Error: {e}")

    def load_dashboard(self):
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()
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
        self.manager.current = "dashboard"

    def logout(self):
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
        toast("Logged out successfully")
        self.manager.current = "login"

# --------------------- ADD CATEGORY ---------------------
class AddCategoryScreen(MDScreen):
    def on_pre_enter(self):
        menu_items = [
            {
                "text": c["text"],
                "viewclass": "OneLineListItem",
                "on_release": lambda x=c: self.set_category_from_menu(x),
            } for c in DEFAULT_CATEGORIES
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.category_dropdown,
            items=menu_items,
            width_mult=4,
            max_height=dp(260),
        )

    def set_category_from_menu(self, cat):
        """Called when a default category is selected."""
        # Ensure 'cat' dict has the correct structure
        name = cat.get("text", "Unnamed")
        color = cat.get("color", "#FFFFFF")

        # ✅ Make sure these IDs exist in the KV file
        self.ids.category_name.text = name
        self.ids.category_color.text = color
        self.menu.dismiss()

    def add_category(self):
        """Send new category to backend or show toast if empty."""
        from kivymd.toast import toast
        from kivymd.app import MDApp
        import requests

        name = self.ids.category_name.text.strip()
        color = self.ids.category_color.text.strip()

        if not name:
            toast("Please enter category name")
            return
        if not color:
            toast("Please enter color (e.g. #E57373)")
            return

        app = MDApp.get_running_app()
        headers = app.get_headers()
        data = {
            "category_name": name,
            "category_color": color,
        }

        try:
            response = requests.post(f"{app.API_BASE}/categories/", data=data, headers=headers)
            if response.status_code in (200, 201):
                toast("Category added successfully!")
                # Clear fields
                self.ids.category_name.text = ""
                self.ids.category_color.text = ""
                # Return to dashboard
                self.manager.current = "dashboard"
            else:
                toast(f"Failed to add category ({response.status_code})")
        except Exception as e:
            toast(f"Error: {e}")

# --------------------- ADD TRANSACTION ---------------------
class AddTransactionScreen(MDScreen):
    def on_pre_enter(self):
        """Load categories when screen opens"""
        self.load_categories()

    def load_categories(self):
        app = MDApp.get_running_app()
        headers = app.get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/categories/", headers=headers)
            if response.status_code == 200:
                data = response.json()
            else:
                toast("Using default categories (no API data)")
                data = [{"category_id": i + 1, "category_name": c["text"]} for i, c in enumerate(DEFAULT_CATEGORIES)]
        except Exception:
            toast("Offline — showing default categories")
            data = [{"category_id": i + 1, "category_name": c["text"]} for i, c in enumerate(DEFAULT_CATEGORIES)]

        menu_items = [
            {
                "text": f"{c['category_name']}",
                "on_release": lambda x=c['category_id'], n=c['category_name']: self.set_category(x, n)
            } for c in data
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.category_dropdown,
            items=menu_items,
            width_mult=4,
        )


    def set_category(self, category_id, name):
        self.ids.category_dropdown.set_item(name)
        self.selected_category = category_id
        self.menu.dismiss()

    def add_transaction(self):
        app = MDApp.get_running_app()
        name = self.ids.name.text.strip()
        amount = self.ids.amount.text.strip()
        category = getattr(self, "selected_category", None)
        date = self.ids.date.text.strip()
        time = self.ids.time.text.strip()

        if not name or not amount or not category:
            toast("Please fill all required fields")
            return

        headers = app.get_headers()
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
            response = requests.post(f"{app.API_BASE}/transactions/", data=data, headers=headers)
            if response.status_code in (200, 201):
                toast("Transaction added successfully!")
                self.manager.current = "dashboard"
            else:
                toast("Failed to add transaction.")
        except Exception as e:
            toast(f"Error: {e}")


if __name__ == "__main__":
    ExpenseTrackerApp().run()
