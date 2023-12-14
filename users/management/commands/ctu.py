from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@sky.pro',
            first_name='Test',
            last_name='Testov',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('12345')
        user.save()
