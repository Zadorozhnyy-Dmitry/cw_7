from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    """Модель юзера"""
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту")
    phone = models.CharField(max_length=35, verbose_name="Телефон", help_text="Укажите телефон", **NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите фото",
        **NULLABLE,
    )
    tg_nick = models.CharField(
        max_length=50,
        verbose_name="Телеграм ник",
        help_text="Укажите телеграм ник",
        **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=35,
        verbose_name="Телеграм chat-id",
        help_text="Укажите телеграм chat-id",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
