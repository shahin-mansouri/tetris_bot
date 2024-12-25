from django.db import models
from datetime import timedelta, datetime

class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    invite_code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    inviter = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='invitees', blank=True, null=True)
    visit_site = models.BooleanField(default=False)

    def generate_invite_code(self):
        import random, string
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(10))

    def save(self, *args, **kwargs):
        # Generate invite code if not set
        if not self.invite_code:
            self.invite_code = self.generate_invite_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username or str(self.telegram_id)


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')
    token = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        # Set default expiration time
        if not self.expires_at:
            self.expires_at = datetime.now() + timedelta(minutes=2)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.token
