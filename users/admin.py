from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "tg_nick",
        "tg_chat_id",
        "is_active",
        "last_login",
    )
