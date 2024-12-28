from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification, UserNotification
from accounts.models import TelegramUser as User


@receiver(post_save, sender=Notification)
def create_user_notifications(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        user_notifications = [
            UserNotification(user=user, notification=instance)
            for user in users
        ]
        UserNotification.objects.bulk_create(user_notifications)
