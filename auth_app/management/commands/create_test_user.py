from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a test user if it does not exist"

    def handle(self, *args, **kwargs):
        # Check if the test user exists
        if not User.objects.filter(username="testuser").exists():
            # Create a test user with a default password
            User.objects.create_user(
                username="testuser", password="testpass", email="test@example.com"
            )
            self.stdout.write(self.style.SUCCESS("Test user created."))
        else:
            self.stdout.write(self.style.SUCCESS("Test user already exists."))
