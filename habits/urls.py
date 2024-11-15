from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitListAPIView, HabitRetrieveAPIView,
                          HabitCreateAPIView, HabitUpdateAPIView,
                          HabitDestroyAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    # вывод списка привычек
    path("", HabitListAPIView.as_view(), name="habits-list"),
    # просмотр одной привычки
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits-retrieve"),
    # создание привычки
    path("create/", HabitCreateAPIView.as_view(), name="habits-create"),
    # изменение одной привычки
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits-update"),
    # удаление одной привычки
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habits-delete", ),
]
