from django.urls import path
from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListAPIView.as_view(), name="payment-list"),  # просмотр списка пользователей
    path("register/", UserCreateAPIView.as_view(), name="users-register"),  # регистрация пользователя

    # эндпоинты для авторизации
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login", ),
    path("api/token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh", ),

]
