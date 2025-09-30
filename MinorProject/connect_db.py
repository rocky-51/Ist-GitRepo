import os
from django.conf import settings
from django.db import connection
os.environ.setdefault('DJ ANGO_SETTINGS_MODULE','minimal_settings')
settings.configure()
def fetch_data_from_table(user):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from user")
        rows=cursor.fetchall()
        return rows
if __name__=='__main__':
    user="user"
    data=fetch_data_from_table(user)
    for row in data:
        print(row)
