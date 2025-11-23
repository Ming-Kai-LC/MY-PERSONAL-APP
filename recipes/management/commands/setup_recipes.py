"""
Management command to set up initial recipe data.
Follows Django best practices for idempotent setup commands.
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from recipes.models import Category


class Command(BaseCommand):
    help = 'Sets up initial categories and sample data for the recipe app'

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-categories',
            action='store_true',
            help='Skip creating default categories',
        )

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Setting up Recipe App...'))

        if not options['skip_categories']:
            self.create_categories()

        self.stdout.write(self.style.SUCCESS('✓ Setup complete!'))

    def create_categories(self):
        """Create default recipe categories."""
        categories = [
            {'name': 'Breakfast', 'description': 'Morning meals and brunch recipes'},
            {'name': 'Lunch', 'description': 'Midday meals'},
            {'name': 'Dinner', 'description': 'Evening meals'},
            {'name': 'Dessert', 'description': 'Sweet treats and desserts'},
            {'name': 'Snacks', 'description': 'Quick bites and appetizers'},
            {'name': 'Italian', 'description': 'Italian cuisine'},
            {'name': 'Mexican', 'description': 'Mexican cuisine'},
            {'name': 'Asian', 'description': 'Asian cuisine'},
            {'name': 'Vegan', 'description': 'Plant-based recipes'},
            {'name': 'Vegetarian', 'description': 'Vegetarian recipes'},
            {'name': 'Quick & Easy', 'description': 'Recipes under 30 minutes'},
            {'name': 'Healthy', 'description': 'Nutritious and healthy options'},
        ]

        created_count = 0
        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'  ✓ Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'  - Category already exists: {category.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Created {created_count} new categories')
        )
