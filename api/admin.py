from django.contrib import admin
from .models import Transaction, Category, Budget, UserProfile

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'type', 'category', 'date']
    list_filter = ['type', 'category', 'date']
    search_fields = ['user__username', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'is_default']  # Removed 'user' from here
    list_filter = ['type', 'is_default']

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'month']
    list_filter = ['month', 'category']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'currency', 'monthly_income']