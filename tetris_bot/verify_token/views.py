from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from telegram_bot.models import Token  # وارد کردن مدل Token از اپ telegram_bot
from django.contrib.auth import login, logout
from django.utils import timezone
from accounts.models import TelegramUser
from urllib.parse import urlencode
from django.views.generic import TemplateView
# import hashlib
# import hmac 
import json
from django.views.decorators.csrf import csrf_exempt
# import time


# def verify_telegram_auth(data):
#     """
#     بررسی صحت امضای داده‌های دریافتی از تلگرام
#     """
#     TOKEN = '7743241678:AAHhYtG5SahoXbW9YjdJZAJKOBCcsUxFMUI'
#     auth_date = int(data.get('auth_date', 0))
#     current_time = int(time.time())

#     # اگر داده‌ها قدیمی باشند، درخواست نامعتبر است
#     if current_time - auth_date > 86400:  # 24 ساعت
#         return False

#     check_hash = data.pop('hash', None)
#     data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
#     secret_key = hashlib.sha256(TOKEN.encode()).digest()
#     hmac_string = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

#     return hmac_string == check_hash

@csrf_exempt
def verify_user(request):
    print("📥 درخواست دریافت شد: ", request.method)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # user_id = data['id']
            # username = data['username']
            # first_name = data['first_name']
            # last_name = data['last_name']
            # print(user_id, first_name, last_name)

            print("📨 داده‌های دریافتی از تلگرام:", data)
        except json.JSONDecodeError:
            print("❌ خطا در تجزیه JSON")
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

        # if not verify_telegram_auth(data):
        #     print("❌ خطا: داده‌های تلگرام نامعتبر هستند.")
        #     return JsonResponse({'success': False, 'error': 'Invalid Telegram data'}, status=403)

        telegram_id = data['id']
        # username = data.get('username', f'user{user_id}')
        try:
            username = data['id']
        except KeyError:
            username = False
             
        first_name = data['first_name']
        last_name = data['last_name']

        user, _ = TelegramUser.objects.get_or_create(telegram_id=telegram_id, defaults={
                'first_name': first_name or "unknown_first_name",
                'last_name': last_name or "unknown_last_name",
                'username': username or "unknown_user",
            })

        login(request, user)
        print("✅ ورود موفق برای:", username)
        return JsonResponse({'success': True})

    print("❌ درخواست نامعتبر (نه POST)")
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)




class Wellcome(TemplateView):
    template_name = "verify_token/index.html"


class VerifyTokenView(View):
    def get(self, request, *args, **kwargs):
        token_value = request.GET.get("token")
        if token_value is None:
            return redirect('home')
        
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
            if create:
                return redirect('wellcome')
            else:
                url = reverse('home')
                query_params = {'create': False}
                url_with_params = f"{url}?{urlencode(query_params)}"
                return HttpResponseRedirect(url_with_params)
            

        except Token.DoesNotExist:
            return HttpResponse("Invalid token!", status=400)
