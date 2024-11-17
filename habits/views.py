from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer


class HabitListAPIView(ListAPIView):
    """Контроллер вывода списка привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination


class HabitPublishedListAPIView(ListAPIView):
    """Контроллер вывода списка публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = CustomPagination


class HabitCreateAPIView(CreateAPIView):
    """Контроллер создания новой привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    # def perform_create(self, serializer):
    #     """Автоматическая запись пользователя в атрибут owner"""
    #     habit = serializer.save()
    #     habit.owner = self.request.user
    #     habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    """Контроллер просмотра одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(UpdateAPIView):
    """Контроллер изменения одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(DestroyAPIView):
    """Контроллер удаления одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
