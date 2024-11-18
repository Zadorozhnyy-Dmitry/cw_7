from celery import shared_task
from django.utils import timezone

from habits.models import Habit

from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_reminder_to_telegram():
    """Отправляет напоминание в телеграмм о привычке"""
    # Выборка пользователей с chat_id
    users = User.objects.all()
    for user in users:
        if user.tg_chat_id:
            print(f'{user.email} - {user.tg_chat_id}')
            # Выборка привычек для данного пользователя
            habits = Habit.objects.filter(owner=user, habit_start__isnull=False)
            for habit in habits:
                # определяем необходимость проводить рассылку сегодня
                days_delta = (timezone.now().date() - habit.habit_start).days
                if days_delta != 0 and days_delta % habit.period == 0:
                    # определяем наступило ли время проводить рассылку
                    if not habit.is_reminder_send and habit.habit_time < timezone.now().time():
                        print('hellt', user.tg_chat_id)
                        message = f'Напоминание: {habit}'
                        send_telegram_message(user.tg_chat_id, message)
                        # Ставлю флаг, что сегодня уже не надо отправлять напоминание
                        habit.is_reminder_send = True
                        habit.save()
