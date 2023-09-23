from django.core.management.base import BaseCommand
from .models import Category  # Import your Category model
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake category data and populate the Category model'

    def handle(self, *args, **kwargs):
        for _ in range(10):  # Create 10 fake category records
            category_name = fake.word()  # Generate a random word as the category name

            Category.objects.create(category_name=category_name)

            self.stdout.write(self.style.SUCCESS(f'Created category: {category_name}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated Category model with fake data'))
