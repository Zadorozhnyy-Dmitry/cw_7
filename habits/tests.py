from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from habits.models import Habit
from rest_framework import status

from habits.serializers import HabitSerializer
from habits.validators import HabitValidate
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


class HabitSerializerTestCase(APITestCase):
    """Тестирование сериализатора"""

    def setUp(self):
        """Фикстуры"""
        self.user = User.objects.create(email='testuser@test.test', password='test')
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Home',
            habit_time='08:00:00',
            action='Съесть яблоко',
            is_enjoyed=True,
            lead_time=120,
        )

    def test_valid_data(self):
        """Проверка правильных значений"""
        data = {
            "owner": self.user.id,
            'place': 'Home',
            'habit_time': timezone.now().time(),
            'action': 'Зарядка',
            'is_enjoyed': False,
            'habit_link': self.habit.pk,
            'period': 3,
            'prize': None,
            'lead_time': 120,
            'is_published': True,
        }
        serializer = HabitSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """Проверка правильных значений"""
        data = {
            'habit_time': '25:70:70',  # неправильное время
            'habit_link': 'some_value',  # должно быть habit.pk
            'period': 'some_value',  # должно быть число
            'lead_time': 'some_value',  # должно быть число
            'is_published': 123,  # должно быть bool
        }
        serializer = HabitSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('habit_time', serializer.errors)
        self.assertIn('habit_link', serializer.errors)
        self.assertIn('period', serializer.errors)
        self.assertIn('lead_time', serializer.errors)
        self.assertIn('is_published', serializer.errors)


class HabitValidaterTestCase(APITestCase):
    """Тесты для валидаторов"""

    def setUp(self):
        self.validator = HabitValidate()
        self.user = User.objects.create(email='testuser@test.test', password='test')
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Home',
            habit_time='08:00:00',
            action='Съесть яблоко',
            is_enjoyed=True,
            lead_time=120,
        )
        self.habit_no_enjoy = Habit.objects.create(
            owner=self.user,
            place='Home',
            habit_time='08:00:00',
            action='Съесть яблоко',
            is_enjoyed=False,
            lead_time=120,
        )

    # Запрет одновременного выбора связанной привычки и указания вознаграждения
    def test_both_habit_link_and_prize(self):
        # проверка ошибки при указании связанной привычки и вознаграждения
        message = 'Нельзя выбрать одновременно и связанную привычку и вознаграждение'
        data = {
            'is_enjoyed': False,
            'habit_link': self.habit,
            'period': 3,
            'prize': 'you win!!!',
            'lead_time': 120,
        }
        with self.assertRaisesMessage(Exception, message):
            self.validator(data)

    def test_only_habit_link(self):
        # Проверяем, что валидатор пропускает данные, если заполнено только одно поле.
        data = {
            'is_enjoyed': False,
            'habit_link': self.habit,
            'period': 3,
            'prize': None,
            'lead_time': 120,
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')

    def test_only_prize(self):
        # Проверяем, что валидатор пропускает данные, если заполнено только одно поле.
        data = {
            'is_enjoyed': False,
            'habit_link': None,
            'period': 3,
            'prize': 'you win!!!',
            'lead_time': 120,
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')

    # В связанные привычки могут попадать только привычки с признаком приятной привычки.
    def test_habit_link_with_no_enjoy(self):
        # проверка ошибки при указании связанной привычки без признака приятной привычки
        message = 'Связанной привычкой можно назначить только приятную привычку'
        data = {
            'is_enjoyed': False,
            'habit_link': self.habit_no_enjoy,
            'period': 3,
            'prize': None,
            'lead_time': 120,
        }
        with self.assertRaisesMessage(Exception, message):
            self.validator(data)

    def test_habit_link_with_is_enjoy(self):
        # проверка валидатора при указании связанной привычки с признаком приятной привычки
        data = {
            'is_enjoyed': False,
            'habit_link': self.habit,
            'period': 3,
            'prize': None,
            'lead_time': 120,
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')

    # Время выполнения должно быть не больше 120 секунд.
    # Проверка валидатора при времени выполнения привычки менее 2 мин было выше
    def test_habit_lead_time_above_120(self):
        # проверка ошибки при времени выполнения привычки более 2 мин
        message = 'Время выполнения привычки должно быть меньше 2 минут (120 секунд)'
        data = {
            'is_enjoyed': False,
            'habit_link': None,
            'period': 3,
            'prize': None,
            'lead_time': 200,
        }
        with self.assertRaisesMessage(Exception, message):
            self.validator(data)

    # У приятной привычки не может быть вознаграждения или связанной привычки.
    def test_enjoy_habit_with_habit_link(self):
        # проверка ошибки указания связанной привычки для приятной привычки
        message = 'У приятной привычки не может быть вознаграждения или связанной привычки'
        data = {
            'is_enjoyed': True,
            'habit_link': self.habit,
            'period': 3,
            'prize': None,
            'lead_time': 120,
        }
        with self.assertRaisesMessage(Exception, message):
            self.validator(data)

    def test_enjoy_habit_with_prize(self):
        # проверка ошибки указания вознаграждения для приятной привычки
        message = 'У приятной привычки не может быть вознаграждения или связанной привычки'
        data = {
            'is_enjoyed': True,
            'habit_link': None,
            'period': 3,
            'prize': "you win!!!",
            'lead_time': 120,
        }
        with self.assertRaisesMessage(Exception, message):
            self.validator(data)

    def test_enjoy_habit(self):
        # проверка что валидатр пропускает приятную привычку без связанной и вознаграждения
        data = {
            'is_enjoyed': False,
            'habit_link': None,
            'period': 3,
            'prize': None,
            'lead_time': 120,
        }
        try:
            self.validator(data)
        except Exception as e:
            self.fail(f'Validator raised exception unexpectedly: {e}')

    # Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    # Проверка валидатора для периода выполнения привычки менее 7 дней было выше
    def test_habit_period(self):
        # проверка ошибки указания периода выполнения привычки
        message = 'Период выполнения привычки должен быть меньше 7 дней'
        data = {
            'is_enjoyed': False,
            'habit_link': None,
            'period': 8,
            'prize': None,
            'lead_time': 120,
        }
        with self.assertRaisesMessage(Exception, message):
            self.validator(data)
