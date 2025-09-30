from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['user_id', 'name', 'password', 'email','created_date']
       read_only_fields = ['name', 'email']

class TransactionsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Transactions
       fields = ['transaction_id', 'category_id', 'user_id', 'transaction_name', 'transaction_amount', 'transaction_date', 'transaction_type']
       read_only_fields = ['transaction_name', 'transaction_date', 'transaction_type', 'transaction_amount']
       
class TransactionsCategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = TransactionCategory
       fields = ['category_id', 'user_id', 'cateogry_name', 'category_color']
       read_only_fields = ['category_name', 'category_color']