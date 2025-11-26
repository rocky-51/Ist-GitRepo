from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TransactionCategory, Transaction
# Register your models here.


# Custom UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


# Category Admin
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'user_id', 'category_name', 'category_color')
    search_fields = ('category_name',)

# Expense Admin
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user_id', 'category_id', 'transaction_name', 'transaction_amount', 'transaction_date', 'transaction_time')
    list_filter = ('category_id',)
    search_fields = ('transaction_name', 'user__email', 'category__category_name')
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TransactionCategory, TransactionCategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)

