from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from config.settings import TEST_USER_MAIL
from courses.models import Course
from subs.models import Sub
from users.models import User


class SubscriptionTestCase(APITestCase):

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

        self.user2 = User.objects.create(
            email=TEST_USER_MAIL,
            first_name='Test',
            last_name='TESTOV',
            is_staff=False,
            is_superuser=False
        )
        self.user2.set_password('12345')
        self.user2.save()

        self.course = Course.objects.create(
            title='test_course',
            description='test'
        )

        self.sub = Sub.objects.create(
            user=self.user2,
            course=self.course
        )

    def test_sub_create(self):
        """Тестирование создания подписки"""

        data = {"course": self.course.id}

        response = self.client.post(
            reverse('subs:create'),
            data=data,
            format='json'
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'user': {
                    'id': self.user.id,
                    'email': 'admin@sky.pro'
                },
                'is_active': True,
                'course': self.course.id
            }
        )

    def test_subs_list(self):
        """Тестирование списка подписок"""

        response = self.client.get(
            reverse('subs:list')
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.sub.id,
                        'user': {
                            'id': self.user2.id,
                            'email': 'trewert132@gmail.com'
                        },
                        'is_active': True,
                        'course': self.course.id
                    }
                ]
            }
        )

    def test_sub_delete(self):
        """Тестирование удаления подписки"""

        response = self.client.delete(
            reverse('subs:delete', args=[self.sub.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
