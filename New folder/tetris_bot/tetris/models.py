# from django.contrib.auth.models import User
from accounts.models import TelegramUser
from django.db import models
from django.utils.timezone import now

class TetrisPlay(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='tetris_sessions')
    play_date = models.DateField(default=now)
    duration = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'play_date') 

    def save(self, *args, **kwargs):
        if self.play_date < now().date():
            self.duration = 0
            self.play_date = now().date()
        super().save(*args, **kwargs)

    def add_play_time(self, minutes):
        if self.duration + minutes > 60:
            raise ValueError("Cannot exceed the daily limit of 60 minutes.")
        self.duration += minutes
        self.save()

    def finish_game(self):
        """
        Call this method to end the game and transfer the score to the Coin model.
        """
        self.transfer_score_to_coin()

    def transfer_score_to_coin(self):
        from home.models import Coin
        coin = Coin.objects.get(user=self.user)
        if coin.is_valid():
            coin.coin_amount += self.score
            self.score = 0  # Reset the score after transferring
            coin.save()

    def __str__(self):
        return f"Tetris session for {self.user.username} on {self.play_date}: {self.duration} minutes"
