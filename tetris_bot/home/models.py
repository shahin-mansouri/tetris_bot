from django.db import models
from accounts.models import TelegramUser
from django.utils.timezone import now
from datetime import timedelta


class Coin(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name="coins")
    coin_amount = models.IntegerField(default=0)
    day = models.IntegerField(default=1)
    next_day_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"User {self.user.username} - {self.coin_amount} coins"
    
    def is_valid(self):
        if self.next_day_time is None:
            return True

        if now() > self.next_day_time + timedelta(days=1):
            self.day = 1
            self.save()  # تغییرات را ذخیره کنید
            return True
        

        return now() > self.next_day_time
