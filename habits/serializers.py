from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import HabitValidate


class HabitSerializer(ModelSerializer):
    """Сериализатор для привычки"""

    class Meta:
        model = Habit
        fields = '__all__'
        ordering_fields = ('id',)
        validators = [HabitValidate(), ]
