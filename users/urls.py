from django.urls import path
from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListAPIView.as_view(), name="payment-list"),  # просмотр списка пользователей
    path("register/", UserCreateAPIView.as_view(), name="users-register"),  # регистрация пользователя
]
