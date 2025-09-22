# minimal_settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "expense_tracker_db",
        "USER": "sunny",
        "PASSWORD": "sp123456",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
INSTALLED_APPS = ['app']

SECRET_KEY = 'dummy'