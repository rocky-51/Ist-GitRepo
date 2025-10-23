from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Important!
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class TransactionCategory(models.Model):
    category_id = models.CharField(primary_key=True,max_length=100)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='TransactionCategory')
    category_name = models.CharField(max_length=100, unique=True)
    category_color = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Transaction(models.Model):
    transaction_id = models.CharField(primary_key=True,max_length=100)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transaction')
    category_id = models.ForeignKey(TransactionCategory, on_delete=models.SET_NULL, null=True, related_name='transaction')
    transaction_name = models.CharField(max_length=200)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    transaction_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"