from django.urls import reverse
from rest_framework.test import APITestCase
from habits.models import Habit
from rest_framework import status
from users.models import User


class HabitModelTestCase(APITestCase):
    """Тест модели привычки"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(email='testuser@test.test', password='test')
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания привычки"""
        habit = Habit.objects.create(
            owner=self.user,
            place='Home',
            habit_time='07:00:00',
            action='Выпить воды',
            prize='Съесть яблоко',
            lead_time=120,
        )
        self.assertEqual(habit.owner, self.user)
        self.assertEqual(habit.place, 'Home')
        self.assertEqual(habit.habit_time, '07:00:00')
        self.assertEqual(habit.action, 'Выпить воды')
        self.assertFalse(habit.is_enjoyed)
        self.assertEqual(habit.habit_link, None)
        self.assertEqual(habit.period, 1)
        self.assertEqual(habit.prize, 'Съесть яблоко')
        self.assertEqual(habit.lead_time, 120)
        self.assertFalse(habit.is_published)


class HabitViewTestCase(APITestCase):
    """Тесты контроллеров привычки"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(email='testuser@test.test', password='test')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Home',
            habit_time='08:00:00',
            action='Съесть яблоко',
            is_enjoyed=True,
            lead_time=120,
        )

    def test_habit_retrieve(self):
        """Тестирование вывода одной привычки"""
        url = reverse('habits:habits-retrieve', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('action'), self.habit.action)

    def test_course_update(self):
        """Тестирование изменения одной привычки"""
        url = reverse('habits:habits-update', args=(self.habit.pk,))
        data = {'lead_time': 100}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lead_time'), 100)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        url = reverse('habits:habits-create')
        data = {
            'place': 'Home',
            'habit_time': '07:00:00',
            'action': 'Зарядка',
            'habit_link': self.habit.pk,
            'lead_time': 120,
            'is_published': True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habits_list(self):
        """Тестирование вывода всех привычек"""
        url = reverse('habits:habits-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.habit.pk,
                    'place': self.habit.place,
                    'habit_time': self.habit.habit_time,
                    'action': self.habit.action,
                    'is_enjoyed': self.habit.is_enjoyed,
                    'period': self.habit.period,
                    'prize': self.habit.prize,
                    'lead_time': self.habit.lead_time,
                    'is_published': self.habit.is_published,
                    'owner': self.user.id,
                    'habit_link': self.habit.habit_link,
                }
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_delete(self):
        """Тестирование удаления одной привычки"""
        url = reverse('habits:habits-delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
