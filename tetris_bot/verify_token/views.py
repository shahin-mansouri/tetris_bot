from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from telegram_bot.models import Token  # وارد کردن مدل Token از اپ telegram_bot
from django.contrib.auth import login, logout
from django.utils import timezone
from accounts.models import TelegramUser
from urllib.parse import urlencode

class VerifyTokenView(View):
    def get(self, request, *args, **kwargs):
        token_value = request.GET.get("token")
        
        # بررسی اینکه آیا توکن موجود است یا خیر
        try:
            token = Token.objects.get(token=token_value)
            
            
            # بررسی اینکه آیا توکن منقضی شده است
            if token.expires_at < timezone.now():
                return HttpResponse("Token has expired!", status=400)

            # بررسی اینکه آیا توکن استفاده شده است
            if token.is_used:
                return HttpResponse("Token has already been used!", status=400)

            # اگر توکن معتبر است
            token.is_used = True
            token.user.visit_site = True
            token.save()
            telegram_id = token.user.telegram_id
            telegram_user, create = TelegramUser.objects.get_or_create(telegram_id=telegram_id, defaults={
                'first_name': token.user.first_name or "unknown_first_name",
                'last_name': token.user.last_name or "unknown_last_name",
                'username': token.user.username or "unknown_user",
            })
            if not request.user.is_authenticated:
                login(request, telegram_user)
            logout(request)
            login(request, telegram_user)
            url = reverse('home')
            query_params = {'create': create}
            url_with_params = f"{url}?{urlencode(query_params)}"
            
            return HttpResponseRedirect(url_with_params)

        except Token.DoesNotExist:
            return HttpResponse("Invalid token!", status=400)
