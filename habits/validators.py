from rest_framework.serializers import ValidationError


class HabitValidate:
    """Проверка правильности заполнения полей привычки"""

    def __init__(
            self,
            is_enjoyed_field='is_enjoyed',
            habit_link_field='habit_link',
            period_field='period',
            prize_field='prize',
            lead_time_field='lead_time',
    ):
        self.is_enjoyed_field = is_enjoyed_field
        self.habit_link_field = habit_link_field
        self.period_field = period_field
        self.prize_field = prize_field
        self.lead_time_field = lead_time_field

    def __call__(self, attrs):
        # Запрет одновременного выбора связанной привычки и указания вознаграждения.
        if attrs[self.habit_link_field] is not None and attrs[self.prize_field] is not None:
            message = 'Нельзя выбрать одновременно и связанную привычку и вознаграждение'
            raise ValidationError(message)
        # Время выполнения должно быть не больше 120 секунд.
        if attrs[self.lead_time_field] > 120:
            message = 'Время выполнения привычки должно быть меньше 2 минут (120 секунд)'
            raise ValidationError(message)
        # В связанные привычки могут попадать только привычки с признаком приятной привычки.
        if attrs[self.habit_link_field] and not attrs[self.habit_link_field].is_enjoyed:
            message = 'Связанной привычкой можно назначить только приятную привычку'
            raise ValidationError(message)
        # У приятной привычки не может быть вознаграждения или связанной привычки.
        if attrs[self.is_enjoyed_field] and (attrs[self.prize_field] or attrs[self.habit_link_field]):
            message = 'У приятной привычки не может быть вознаграждения или связанной привычки'
            raise ValidationError(message)
        # # Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
        if attrs[self.period_field] > 7:
            message = 'Период выполнения привычки должен быть меньше 7 дней'
            raise ValidationError(message)
