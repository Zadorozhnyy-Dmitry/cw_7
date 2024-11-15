from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls", namespace="users")),  # маршрут к приложению Пользователей
    path("habits/", include("habits.urls", namespace="habits")),  # маршрут к приложению Привычки
]
