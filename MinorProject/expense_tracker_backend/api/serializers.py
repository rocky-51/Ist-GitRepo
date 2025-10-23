from rest_framework import serializers
from .models import CustomUser, TransactionCategory, Transaction

# ---------- User Serializer ----------
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['user_id', 'name', 'email', 'password', 'created_at']
        read_only_fields = ['user_id', 'created_at']

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
        fields = ['category_id', 'user_id', 'category_name', 'category_color']
        read_only_fields = ['category_id', 'category_name']


# ---------- Expense Serializer ----------
class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=TransactionCategory.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Transaction
        fields = [
            'transaction_id', 'user_id', 'category_id',
            'transaction_name', 'transaction_amount', 'transaction_date', 'tansaction_time'
        ]
        read_only_fields = ['transaction_id', 'transaction_date', 'user_id']
