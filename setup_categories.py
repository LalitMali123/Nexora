import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from api.models import Category

# Global categories for all users
global_categories = [
    # Expense categories
    ('Food', '🍕', 'expense'),
    ('Transport', '🚗', 'expense'),
    ('Shopping', '🛍️', 'expense'),
    ('Entertainment', '🎬', 'expense'),
    ('Bills', '💡', 'expense'),
    ('Healthcare', '🏥', 'expense'),
    ('Education', '📚', 'expense'),
    ('Rent', '🏠', 'expense'),
    ('Utilities', '💧', 'expense'),
    ('Insurance', '🛡️', 'expense'),
    ('Other', '💰', 'expense'),
    
    # Income categories
    ('Salary', '💼', 'income'),
    ('Freelance', '💻', 'income'),
    ('Investment', '📈', 'income'),
    ('Gift', '🎁', 'income'),
    ('Bonus', '🎉', 'income'),
    ('Refund', '↩️', 'income'),
    ('Other Income', '💰', 'income'),
]

print("Creating global categories...")
for name, icon, type in global_categories:
    category, created = Category.objects.get_or_create(
        name=name,
        type=type,
        defaults={'icon': icon, 'is_default': True}
    )
    if created:
        print(f"✓ Created: {name} ({type})")
    else:
        print(f"○ Already exists: {name}")

print(f"\n✅ Total global categories: {Category.objects.count()}")