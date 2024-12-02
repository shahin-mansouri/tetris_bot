from django.db import models
from accounts.models import TelegramUser


class Coin(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name="coins")
    coin_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"User {self.user.username} - {self.coin_amount} coins"