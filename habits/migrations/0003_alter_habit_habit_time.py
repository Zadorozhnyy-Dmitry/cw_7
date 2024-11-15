# Generated by Django 5.1.3 on 2024-11-14 21:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit_time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Время, когда необходимо выполнять привычку', verbose_name='Время'),
        ),
    ]