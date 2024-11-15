# Generated by Django 5.1.3 on 2024-11-15 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit_time',
            field=models.TimeField(default=datetime.time(18, 31, 59, 427351), help_text='Время, когда необходимо выполнять привычку', verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='lead_time',
            field=models.PositiveSmallIntegerField(help_text='Время, которое предположительно потратится на выполнение привычки в секундах', verbose_name='Время на выполнение'),
        ),
    ]