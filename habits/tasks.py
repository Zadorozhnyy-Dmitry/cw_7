from celery import shared_task
from django.utils import timezone

from habits.models import Habit

from datetime import timedelta


@shared_task
def send_reminder_to_telegram():
    """Отправляет напоминание в телеграмм о привычке"""
    habits = Habit.objects.filter(owner__isnull=False, habit_start__isnull=False)
    for habit in habits:
        # определяем необходимость проводить рассылку сегодня
        days_delta = (habit.habit_start - timezone.now().date()).days
        if days_delta != 0 and days_delta % habit.period == 0:
            # определяем наступило ли время проводить рассылку
            if habit.habit_time < timezone.now().time():
                print('reminder')
