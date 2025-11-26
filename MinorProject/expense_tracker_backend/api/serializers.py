from rest_framework import serializers
from .models import CustomUser, TransactionCategory, Transaction

# ---------- User Serializer ----------
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['user_id', 'name', 'email', 'password', 'date_joined']
        read_only_fields = ['user_id', 'date_joined']


    def create(self, validated_data):
        # Create user with hashed password
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


# ---------- Category Serializer ----------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = ['user_id', 'category_id', 'category_name', 'category_color']  # use actual model field names
        read_only_fields = ['category_id','user_id']


# ---------- Expense Serializer ----------

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'transaction_id',
            'transaction_name',
            'transaction_amount',
            'transaction_date',
            'transaction_time',
            'category_id',
            'user_id'
        ]
        read_only_fields = ['transaction_id', 'transaction_date', 'transaction_time', 'user_id']


