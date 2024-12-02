from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


class UserViewTestCase(APITestCase):
    """Тесты контроллеров привычки"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(email='testuser@test.test', password='test')

    def test_user_create(self):
        """Тестирование регистрации пользователя"""
        url = reverse('users:users-register')
        data = {
            'email': 'testuser1@test.test',
            'password': 'test',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_users_list(self):
        """Тестирование вывода всех пользователей"""
        self.client.force_authenticate(user=self.user)
        url = reverse('users:users-list')
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = [
            {
                'id': self.user.id,
                'email': 'testuser@test.test',
                'is_active': True,
                'is_superuser': False,
                'tg_nick': None,
                'tg_chat_id': None,
                'phone': None,
                'last_login': None
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
