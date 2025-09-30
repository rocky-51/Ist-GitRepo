from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class User(models.Model):
   user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=50, blank=True)
   created_at = models.DateField(auto_now_add=True)
   password = models.IntegerField(blank=True)
   def __str__(self):
       return f"{self.name} - {self.email}"

class Transactions(models.Model):
   category_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='transaction_category')
   user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
   cateogry_name = models.CharField(max_length=100)
   category_color= models.CharField(max_length=100)
   def __str__(self):
       return f"{self.cateogry_name} - {self.category_color}"
   
class TransactionCategory(models.Model):
   transaction_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='transactions')
   category_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='transaction_category')
   user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
   transaction_name = models.CharField(max_length=100)
   transaction_amount = models.IntegerField(blank=True)
   transaction_date = models.DateField(auto_now_add=True)
   transaction_type= models.CharField(max_length=100)
   def __str__(self):
       return f"{self.transaction_name} - {self.transaction_date} - {self.transaction_amount} - {self.transaction_type}"

