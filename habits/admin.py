from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'place',
        'action',
        'is_enjoyed',
        'habit_link',
        'prize',
        'is_published',
    )
