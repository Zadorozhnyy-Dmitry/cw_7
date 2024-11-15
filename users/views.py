from rest_framework.generics import ListAPIView, CreateAPIView

from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer


class UserListAPIView(ListAPIView):
    """Контроллер вывода списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    """Контроллер для регистрации пользователя"""

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """Шифрование пароля при регистрации пользователя"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
