from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)  # Or models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'your_table_name_in_mysql'
        managed = False  # Set to False if you don't want Django to manage the table schema

# from your_app.models import YourTableName

# # Get all records from the table
# all_records = YourTableName.objects.all()

# for record in all_records:
#     print(f"Name: {record.name}, Email: {record.email}")
# from your_app.models import YourTableName

# new_record = YourTableName(name='John Doe', email='john.doe@example.com')
# new_record.save()