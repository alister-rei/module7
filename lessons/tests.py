from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from config.settings import TEST_USER_MAIL
from courses.models import Course
from lessons.models import Lesson
from users.models import User


class LessonModeratorTestCase(APITestCase):

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

        self.course = Course.objects.create(
            title='test_course',
            description='test'
        )

        self.lesson = Lesson.objects.create(
            title='test_lesson',
            description='test',
            course=self.course
        )

    def test_lesson_create(self):
        """#1    Test lesson creating"""

        data = {
            "title": "test course 3",
            "description": "test course 3",
            "course": 1
        }

        response = self.client.post(
            reverse('lessons:create'),
            data=data,
            format='json'
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            1
        )

        self.assertEqual(
            response.json(),
            {
                "detail": "У вас недостаточно прав для выполнения данного действия."
            }
        )

    def test_get_lessons_list(self):
        """#2    Test for getting list of lessons"""

        response = self.client.get(
            reverse('lessons:list')
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
                        'id': self.lesson.id,
                        'description': 'test',
                        'owner': None,
                        'title': 'test_lesson',
                        'image': None,
                        'video': None,
                        'course': self.course.id
                    }
                ]
            }
        )

    def test_retrieve_lesson(self):
        """#3    Test for getting lesson"""

        retrieve_url = reverse('lessons:view', args=[self.lesson.id])
        response = self.client.get(retrieve_url)

        # print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.id,
                'description': 'test',
                'owner': None,
                'title': 'test_lesson',
                'image': None,
                'video': None,
                'course': self.course.id
            }

        )

    def test_update_lesson(self):
        """#4    Test for update lesson"""

        update_url = reverse('lessons:edit', args=[self.lesson.id])
        updated_data = {
            "title": "Updated Lesson",
            "description": "This is an updated lesson"
        }

        response = self.client.patch(update_url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, updated_data['title'])
        self.assertEqual(self.lesson.description, updated_data['description'])

    def test_delete_lesson(self):
        """#5    Test for delete lesson"""
        delete_url = reverse('lessons:delete', args=[self.lesson.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Lesson.objects.all().count(), 1)


class LessonMemberTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.user = User.objects.create(
            email='test@sky.pro',
            first_name='test',
            last_name='testov',
            is_staff=False,
            is_superuser=False
        )
        self.user.set_password('12345')
        self.user.save()

        token_url = reverse_lazy('users:token_obtain_pair')
        token_response = self.client.post(token_url, data={'email': 'test@sky.pro', 'password': '12345'})
        token = token_response.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='test_course',
            description='test',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='test_lesson',
            description='test',
            course=self.course,
            owner=self.user
        )

    def test_lesson_create(self):
        """#1    Test lesson creating"""

        data = {
            "title": "test course 3",
            "description": "test course 3",
            "course": self.course.id
        }

        response = self.client.post(
            reverse('lessons:create'),
            data=data,
            format='json'
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

        ids = response.json()['id']

        self.assertEqual(
            response.json(),
            {
                'id': ids,
                'description': 'test course 3',
                'owner': {
                    'id': self.user.id,
                    'email': 'test@sky.pro'
                },
                'title': 'test course 3',
                'image': None,
                'video': None,
                'course': self.course.id
            }
        )

    def test_get_lessons_list(self):
        """#2    Test for getting list of lessons"""

        response = self.client.get(
            reverse('lessons:list')
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
                        'id': self.lesson.id,
                        'description': 'test',
                        'owner': {
                            'id': self.user.id,
                            'email': 'test@sky.pro'
                        },
                        'title': 'test_lesson',
                        'image': None,
                        'video': None,
                        'course': self.course.id
                    }
                ]
            }
        )

    def test_update_lesson(self):
        """#3    Test for getting lesson"""

        update_url = reverse('lessons:edit', args=[self.lesson.id])
        updated_data = {
            "title": "Updated Lesson",
            "description": "This is an updated lesson"
        }

        response = self.client.patch(update_url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, updated_data['title'])
        self.assertEqual(self.lesson.description, updated_data['description'])

    def test_delete_lesson(self):
        delete_url = reverse('lessons:delete', args=[self.lesson.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)
