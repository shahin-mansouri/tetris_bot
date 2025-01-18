from django.db import models
from accounts.models import TelegramUser

class Youtube(models.Model):
    """Model definition for Youtube."""
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='youtube_subscriptions')
    is_sub = models.BooleanField(default=False)
    channel_url = models.URLField(max_length=200, blank=True, null=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # فیلدهای جدید برای ذخیره‌سازی توکن‌ها
    access_token = models.CharField(max_length=255, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    token_expiry = models.DateTimeField(blank=True, null=True)

    class Meta:
        """Meta definition for Youtube."""
        verbose_name = 'Youtube'
        verbose_name_plural = 'Youtubes'
        ordering = ['-subscription_date']

    def __str__(self):
        """Unicode representation of Youtube."""
        return f'{self.user.username} - {self.is_sub}'