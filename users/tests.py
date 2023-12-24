from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from config.settings import TEST_USER_MAIL
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        group, _ = Group.objects.get_or_create(name='moderator')

        self.user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password('12345')
        self.user.groups.add(group)
        self.user.save()

        token_url = reverse_lazy('users:token_obtain_pair')
        token_response = self.client.post(token_url, data={'email': 'admin@sky.pro', 'password': '12345'})
        token = token_response.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """#1    Test user creating"""

        data = {
            "email": TEST_USER_MAIL,
            "password": "12345",
            "first_name": "Test",
            "last_name": "Testov",
            "phone": None,
            "country": None,
            "city": None,
            "avatar": None
        }

        response = self.client.post(
            reverse('users:create'),
            data=data,
            format='json'
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.all().count(),
            2
        )

    def test_get_users_list(self):
        """#2    Test for getting list of users"""

        response = self.client.get(
            reverse('users:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response.json())

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.user.id,
                        'email': 'admin@sky.pro',
                        'is_staff': True,
                        'is_superuser': True,
                        'first_name': 'Admin',
                        'last_name': 'SkyPro',
                        'phone': None,
                        'country': None,
                        'city': None,
                        'avatar': None
                    }
                ]
            }
        )
