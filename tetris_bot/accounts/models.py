from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class TelegramUser(AbstractUser):
    telegram_id = models.BigIntegerField(default=123, unique=True)
    username    = models.CharField(max_length=50, unique=True)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    password    = models.CharField(
                                   max_length=128,
                                   default=make_password("defaultpassword")  # پسورد هش شده
                                        )

    # Adding related_name to prevent reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group', related_name='telegramuser_set', blank=True, verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='telegramuser_set', blank=True, verbose_name='user permissions'
    )

    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} (@{self.username})"

