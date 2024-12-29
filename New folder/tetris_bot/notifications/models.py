from django.db import models
from django.utils import timezone
from accounts.models import TelegramUser as User

class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title

    def get_time_ago(self):
        from django.utils.timesince import timesince
        return timesince(self.timestamp) + " ago"

class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.notification.title} for {self.user.username}"

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save()
