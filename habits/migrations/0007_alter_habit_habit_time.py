# Generated by Django 5.1.3 on 2024-11-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_alter_habit_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit_time',
            field=models.TimeField(auto_now=True, help_text='Время, когда необходимо выполнять привычку', verbose_name='Время'),
        ),
    ]