from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import TelegramUser
from notifications.models import Notification
from home.models import Coin
from telegram_bot.models import User
from notifications.models import Notification, UserNotification


class ProfileView(TemplateView):
    template_name = "accounts/wallet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context['notifications'] = Notification.objects.all()
        user = self.request.user
        invited_users = User.objects.filter(inviter__telegram_id=user.telegram_id)
        telegram_ids = list(invited_users.values_list('telegram_id', flat=True))
        
        similar_users = TelegramUser.objects.filter(telegram_id__in=telegram_ids)
        
        s_u_coins = Coin.objects.filter(user__in=similar_users)
        context['invitees'] = s_u_coins
        context['user_notifications'] = UserNotification.objects.filter(user=user)
        return context
    
from django.contrib import auth
def logout(request):
    auth.logout(request)
    return HttpResponse('Log out.')
