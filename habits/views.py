from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer


class HabitListAPIView(ListAPIView):
    """Контроллер вывода списка привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('is_enjoyed', 'period', 'is_published',)
    ordering_fields = ['id', ]
    pagination_class = CustomPagination


class HabitPublishedListAPIView(ListAPIView):
    """Контроллер вывода списка публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('owner', 'action', 'period',)
    ordering_fields = ['owner', 'id', ]


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
