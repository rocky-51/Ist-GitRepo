import pymysql
pymysql.install_as_MySQLdb()
import os
import django
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()
from models import Student
from django.core.management import call_command
call_command('makemigrations', 'app')
call_command('migrate')
Student.objects.create(name="Ravi", age=22)
for s in Student.objects.all():
    print(s.name, s.age)