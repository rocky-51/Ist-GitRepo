from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from kivy.metrics import dp
from kivymd.toast import toast
from kivy.lang import Builder
from screens.splash_screen import splash_screen
from screens.helper import expensetracker
from screens.register_screen import register_screen
from screens.profile_screen import profile_screen
from screens.change_password_screen import change_password_screen
from screens.dashboard_screen import dashboard_screen 
from screens.add_category_screen import add_category_screen
from screens.add_transaction_screen import add_transaction_screen
from screens.transactions_sceen import transactions_screen
from screens.edit_transaction_screen import edit_transaction_screen
from kivy.uix.screenmanager import FadeTransition
from kivy.clock import Clock
from kivy.animation import Animation

import requests
import json
import os
import base64

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
    current_user_id = None
    
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
        Builder.load_string(profile_screen)
        Builder.load_string(change_password_screen)
        Builder.load_string(dashboard_screen)
        Builder.load_string(add_category_screen)
        Builder.load_string(add_transaction_screen)
        Builder.load_string(edit_transaction_screen)
        Builder.load_string(transactions_screen)


        sm = MDScreenManager(transition=FadeTransition(duration=0.5)) 
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(ChangePasswordScreen(name="change_password"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(AddCategoryScreen(name="add_category"))
        sm.add_widget(AddTransactionScreen(name="add_transaction"))
        sm.add_widget(EditTransactionScreen(name="edit_transaction"))
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
        Clock.schedule_once(self.start_fade_out, 10)

    def start_fade_out(self, *args):
        fade_out = Animation(opacity=0, duration=1)
        fade_out.bind(on_complete=lambda *x: self.go_to_login())
        fade_out.start(self)

    def go_to_login(self, *args):
        self.manager.current = "login"
        self.opacity = 1  # reset opacity for next time

# --------------------- LOGIN ---------------------
class LoginScreen(MDScreen):

    def get_user_id_from_token(self, token):
        """Decode JWT without verifying signature and extract user_id."""
        try:
            payload_part = token.split(".")[1]
            padded = payload_part + "=" * (-len(payload_part) % 4)
            decoded = base64.urlsafe_b64decode(padded)
            data = json.loads(decoded)
            return data.get("user_id")
        except:
            return None
        
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

            print("LOGIN RESPONSE:", response.text)

            if response.status_code == 200:
                data = response.json()
                access = data.get("access")
                refresh = data.get("refresh")

                # ✅ EXTRACT USER ID FROM JWT
                user_id = self.get_user_id_from_token(access)

                print("DECODED USER ID =", user_id)

                if not user_id:
                    toast("Login failed — couldn't decode user ID")
                    return

                with open(TOKEN_FILE, "w") as f:
                    json.dump({"access": access, "refresh": refresh, "user_id": user_id}, f)

                # Store in app instance
                app = MDApp.get_running_app()
                app.current_user_id = user_id

                toast("Login successful!")
                self.manager.current = "dashboard"
            else:
                toast("Invalid credentials")
        except Exception as e:
            toast(f"Error: {e}")

# --------------------- PROFILE SCREEN ---------------------
class ProfileScreen(MDScreen):

    def on_pre_enter(self):
        app = MDApp.get_running_app()
        headers = app.get_headers()

        response = requests.get(f"{app.API_BASE}/profile/", headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.ids.user_name.text = data.get("name", "")
            self.ids.user_email.text = data.get("email", "")

    def update_profile(self):
        app = MDApp.get_running_app()
        headers = app.get_headers()

        payload = {
            "name": self.ids.user_name.text,
            "email": self.ids.user_email.text,
        }

        response = requests.patch(f"{app.API_BASE}/profile/update-profile/", json=payload, headers=headers)

        if response.status_code == 200:
            toast("Profile updated!")
        else:
            toast(f"Update failed: {response.text}")

    def delete_account(self):
        app = MDApp.get_running_app()
        headers = app.get_headers()

        response = requests.delete(f"{app.API_BASE}/profile/delete-account", headers=headers)

        if response.status_code == 204:
            toast("Account deleted!")

            # Clear token
            if os.path.exists(TOKEN_FILE):
                os.remove(TOKEN_FILE)

            self.manager.current = "login"
        else:
            toast(f"Delete failed: {response.text}")

    def load_dashboard(self):
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/expenses/", headers=headers)
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

# --------------------- CHANGE PASSWORD SCREEN ---------------------
class ChangePasswordScreen(MDScreen):

    def change_password(self):
        from kivymd.toast import toast
        from kivymd.app import MDApp
        import requests

        current = self.ids.current_password.text.strip()
        new = self.ids.new_password.text.strip()
        confirm = self.ids.confirm_password.text.strip()

        if not current or not new or not confirm:
            toast("Fill all fields")
            return

        if new != confirm:
            toast("New passwords do not match")
            return

        app = MDApp.get_running_app()
        headers = app.get_headers()

        payload = {
            "current_password": current,
            "new_password": new,
        }

        url = f"{app.API_BASE}/profile/change-password/"

        try:
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                toast("Password updated successfully!")
                self.manager.current = "profile"
            else:
                toast(f"Failed: {response.text}")

        except Exception as e:
            toast(f"Error: {e}")
    
    def load_dashboard(self):
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/expenses/", headers=headers)
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
            response = requests.get(f"{app.API_BASE}/expenses/", headers=headers)
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
        self.load_transactions()

    def get_headers(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                data = json.load(f)
                access = data.get("access")
                return {"Authorization": f"Bearer {access}"}
        return {}

    def open_edit_transaction(self):
        self.dialog.dismiss()
        tx = self.selected_transaction

        screen = self.manager.get_screen("edit_transaction")

        screen.transaction_id = tx["transaction_id"]
        screen.ids.edit_name.text = tx["transaction_name"]
        screen.ids.edit_amount.text = str(tx["transaction_amount"])
        screen.ids.edit_date.text = tx["transaction_date"]
        screen.ids.edit_time.text = tx["transaction_time"]

        self.manager.current = "edit_transaction"


    def delete_transaction(self):

        tx = self.selected_transaction
        transaction_id = tx["transaction_id"]

        app = MDApp.get_running_app()
        headers = app.get_headers()

        response = requests.delete(
            f"{app.API_BASE}/expenses/{transaction_id}/",
            headers=headers
        )

        if response.status_code in (200, 204):
            toast("Transaction deleted!")
            self.dialog.dismiss()
            self.load_transactions()
        else:
            toast("Failed to delete")



    def load_dashboard(self):
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/expenses/", headers=headers)
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
    
    def load_transactions(self):

        app = MDApp.get_running_app()
        headers = app.get_headers()

        try:
            response = requests.get(f"{app.API_BASE}/expenses/", headers=headers)
            print("Transaction API Response:", response.status_code, response.text)

            if response.status_code != 200:
                toast("Failed to load transactions")
                return

            transactions = response.json()

        except Exception as e:
            toast("Error loading data")
            print(e)
            return

        # Clear list
        self.ids.transactions_list.clear_widgets()

        # Add items
        for tx in transactions:
            item = OneLineListItem(
                text=f"{tx['transaction_name']} • ₹{tx['transaction_amount']} • {tx['transaction_date']}",
                on_release=lambda x, t=tx: self.open_transaction_details(t)
            )
            self.ids.transactions_list.add_widget(item)

    def open_transaction_details(self, tx):
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton

        self.selected_transaction = tx  # store globally

        self.dialog = MDDialog(
            title="Transaction Options",
            text=(
                f"Name: {tx['transaction_name']}\n"
                f"Amount: ₹{tx['transaction_amount']}\n"
                f"Date: {tx['transaction_date']}\n"
                f"Time: {tx['transaction_time']}\n"
                f"Category ID: {tx['category_id']}"
            ),
            buttons=[
                MDFlatButton(text="Edit", on_release=lambda x: self.open_edit_transaction()),
                MDFlatButton(text="Delete", on_release=lambda x: self.delete_transaction()),
                MDFlatButton(text="Close", on_release=lambda x: self.dialog.dismiss()),
            ]
        )
        self.dialog.open()



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

        # ✅ FIX: include user_id in payload
        data = {
            "category_name": name,
            "category_color": color,
            "user_id": app.current_user_id
        }

        try:
            response = requests.post(
                f"{app.API_BASE}/categories/",
                json=data,
                headers=headers,
                timeout=5
            )

            print("Response:", response.status_code, response.text)

            if response.status_code in (200, 201):
                toast("Category added successfully!")
                self.ids.category_name.text = ""
                self.ids.category_color.text = ""
                self.manager.current = "dashboard"
            else:
                error = response.json()
                if "category_name" in error:
                    toast("Category already exists!")
                else:
                    toast(f"Failed: {response.text}")
    
            if response.status_code == 400:
                if "category_name" in response.json():
                    toast("Category already exists!")
                    return


        except Exception as e:
            toast(f"Error: {e}")



# --------------------- ADD TRANSACTION ---------------------
class AddTransactionScreen(MDScreen):

    menu = None   # IMPORTANT

    def on_pre_enter(self):
        """Auto-fill date/time and load categories safely."""
        from datetime import datetime
        now = datetime.now()
        self.ids.transaction_date.text = now.strftime("%Y-%m-%d")
        self.ids.transaction_time.text = now.strftime("%H:%M:%S")

        self.selected_category_id = None
        # self.menu = None  # Reset menu every time user enters
        self.load_categories()


    # ------------------------------
    # OPEN CATEGORY DROPDOWN
    # ------------------------------
    def open_category_menu(self):
        if self.menu:
            self.menu.open()
        else:
            from kivymd.toast import toast
            toast("No categories available")

    def set_category(self, category_obj):
        self.ids.category_name.text = category_obj["category_name"]
        self.selected_category_id = category_obj["category_id"]

        if self.menu:
            self.menu.dismiss()


    # ------------------------------
    # ADD TRANSACTION
    # ------------------------------
    def add_transaction(self):
        from kivymd.toast import toast
        from kivymd.app import MDApp
        import requests

        name = self.ids.transaction_name.text
        amount = self.ids.transaction_amount.text
        date = self.ids.transaction_date.text
        time = self.ids.transaction_time.text
        category_id = getattr(self, "selected_category_id", None)

        if not name or not amount or not category_id:
            toast("Please fill all required fields!")
            return

        app = MDApp.get_running_app()
        headers = app.get_headers()

        payload = {
            "transaction_name": name,
            "transaction_amount": amount,
            "transaction_date": date,
            "transaction_time": time,
            "category_id": category_id,
        }

        print("Sending Transaction:", payload)

        response = requests.post(
            f"{app.API_BASE}/expenses/",
            json=payload,
            headers=headers
        )

        print("Add Response:", response.status_code, response.text)

        if response.status_code in (200, 201):
            toast("Transaction Added Successfully!")
            self.manager.current = "transactions"
        else:
            toast(f"Error: {response.text}")
            
    def load_dashboard(self):
        app = MDApp.get_running_app()
        headers = MDApp.get_running_app().get_headers()
        try:
            response = requests.get(f"{app.API_BASE}/expenses/", headers=headers)
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
    
    def load_categories(self):

        print("\n----- LOADING CATEGORIES -----")

        app = MDApp.get_running_app()
        headers = app.get_headers()
        print("APP.USER_ID =", app.current_user_id)

        try:
            response = requests.get(f"{app.API_BASE}/categories/", headers=headers)
            print("RAW CATEGORY API RESPONSE:", response.text)
            categories = response.json()
        except Exception as e:
            print("ERROR FETCHING:", e)
            categories = []

        # Normalize user_id key
        for c in categories:
            if "user" in c and "user_id" not in c:
                c["user_id"] = c["user"]

        print("NORMALIZED:", categories)

        # Filter categories for current user
        filtered = [c for c in categories if str(c.get("user_id")) == str(app.current_user_id)]
        print("FILTERED:", filtered)

        if not filtered:
            toast("No categories found for this user.")
            self.menu = None
            return

        # Build menu items
        menu_items = [
            {
                "text": c["category_name"],
                "viewclass": "OneLineListItem",
                "on_release": lambda x=c: self.set_category(x)
            } for c in filtered
        ]

        print("MENU ITEMS:", menu_items)

        # Build dropdown
        self.menu = MDDropdownMenu(
            caller=self.ids.category_name,
            items=menu_items,
            width_mult=4,
        )

        print("DROPDOWN CREATED SUCCESSFULLY.")



# --------------------- EDIT TRANSACTION SCREEN ---------------------
class EditTransactionScreen(MDScreen):
    transaction_id = None

    def update_transaction(self):

        app = MDApp.get_running_app()
        headers = app.get_headers()

        payload = {
            "transaction_name": self.ids.edit_name.text,
            "transaction_amount": self.ids.edit_amount.text,
            "transaction_date": self.ids.edit_date.text,
            "transaction_time": self.ids.edit_time.text,
        }

        response = requests.put(
            f"{app.API_BASE}/expenses/{self.transaction_id}/",
            json=payload,
            headers=headers
        )

        if response.status_code in (200, 202):
            toast("Transaction updated!")

            # FIX 🟢 refresh transaction list
            tx_screen = self.manager.get_screen("transactions")
            tx_screen.load_transactions()

            self.manager.current = "transactions"
        else:
            toast("Failed to update transaction")

    def go_back_to_transactions(self):
        tx_screen = self.manager.get_screen("transactions")
        tx_screen.load_transactions()  # refresh list
        self.manager.current = "transactions"


if __name__ == "__main__":
    ExpenseTrackerApp().run()
