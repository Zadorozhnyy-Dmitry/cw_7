# Generated by Django 5.1.3 on 2024-11-14 21:19

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, help_text='Место, в котором необходимо выполнять привычку', max_length=150, null=True, verbose_name='Место')),
                ('habit_time', models.TimeField(default=datetime.time(21, 19, 6, 718732), help_text='Время, когда необходимо выполнять привычку', verbose_name='Время')),
                ('action', models.CharField(help_text='Действие, которое представляет собой привычка', max_length=150, verbose_name='Действие')),
                ('is_enjoyed', models.BooleanField(default=False, help_text='Укажите, является ли привычка приятной', verbose_name='Признак приятной привычки')),
                ('period', models.PositiveSmallIntegerField(default=1, help_text='Периодичность выполнения привычки для напоминания в днях', verbose_name='Периодичность')),
                ('prize', models.CharField(blank=True, help_text='Чем пользователь должен себя вознаградить после выполнения', max_length=150, null=True, verbose_name='Вознаграждение')),
                ('lead_time', models.PositiveSmallIntegerField(default=1, help_text='Время, которое предположительно потратится на выполнение привычки в секундах', verbose_name='Время на выполнение')),
                ('is_published', models.BooleanField(default=False, help_text='Привычки можно публиковать в общий доступ', verbose_name='Признак публичности')),
                ('habit_link', models.ForeignKey(blank=True, help_text='Привычка, которая связана с этой привычкой', null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]