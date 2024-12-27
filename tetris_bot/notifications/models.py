from django.db import models
from django.utils import timezone
from accounts.models import TelegramUser


class Notification(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='notifications_user')
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    is_read = models.BooleanField(default=False)
    sent_to_all = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_time_ago(self):
        from django.utils import timezone
        from datetime import timedelta

        time_diff = timezone.now() - self.timestamp
        if time_diff < timedelta(minutes=1):
            return "Just now"
        elif time_diff < timedelta(hours=1):
            return f"{time_diff.seconds // 60} minutes ago"
        elif time_diff < timedelta(days=1):
            return f"{time_diff.seconds // 3600} hours ago"
        else:
            return f"{time_diff.days} days ago"
