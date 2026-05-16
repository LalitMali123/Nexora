from django.core.management.base import BaseCommand
from django.core.management import call_command
from api.models import Category

class Command(BaseCommand):
    help = 'Setup database with migrations and categories'

    def handle(self, *args, **options):
        self.stdout.write("Running migrations...")
        call_command('migrate', interactive=False)
        
        self.stdout.write("Creating categories...")
        categories = [
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
            ('Salary', '💼', 'income'),
            ('Freelance', '💻', 'income'),
            ('Investment', '📈', 'income'),
            ('Gift', '🎁', 'income'),
        ]
        
        created_count = 0
        for name, icon, type in categories:
            obj, created = Category.objects.get_or_create(
                name=name,
                type=type,
                defaults={'icon': icon, 'is_default': True}
            )
            if created:
                created_count += 1
                self.stdout.write(f"  Created: {name}")
            else:
                self.stdout.write(f"  Exists: {name}")
        
        self.stdout.write(self.style.SUCCESS(f"\n✅ Setup complete!"))
        self.stdout.write(self.style.SUCCESS(f"   Categories: {Category.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"   Newly created: {created_count}"))
