from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = User
        fields = ('id', 'email', 'is_active', 'is_superuser', 'tg_nick', 'tg_chat_id', 'phone', 'last_login',)


class UserCreateSerializer(ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    class Meta:
        model = User
        fields = ("email", "password",)
