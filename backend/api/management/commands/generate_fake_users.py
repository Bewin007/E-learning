from django.core.management.base import BaseCommand
from api.models import User  # Import your Category model
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake user data and populate the User model'

    def handle(self, *args, **kwargs):
        for _ in range(100):  # Create 10 fake user records
            username = fake.user_name()
            email = fake.email()
            password = fake.password(length=8)
            first_name = fake.first_name()
            last_name = fake.last_name()
            profile_pic = 'profile_pic/default.jpg'
            user_type = fake.random_element(elements=('Admin', 'User', 'Moderator', 'Guest'))
            join_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
            last_login_timestamp = fake.date_time_this_decade()
            dob = fake.date_of_birth(minimum_age=18, maximum_age=65)

            User.objects.create(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                profile_pic=profile_pic,
                user_type=user_type,
                join_date=join_date,
                last_login_timestamp=last_login_timestamp,
                dob=dob
            )

            self.stdout.write(self.style.SUCCESS(f'Created user: {username}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated User model with fake data'))