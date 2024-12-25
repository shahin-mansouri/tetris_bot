from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from accounts.models import TelegramUser
from .models import Coin

def home(request):
    # اگر کاربر وارد شده باشد، فقط صفحه را نمایش می‌دهیم
    if request.user.is_authenticated:
        context = dict()
        coins, create = Coin.objects.get_or_create(user=request.user)
        context['coins'] = coins
        context['day'] = coins.day
        context['next_day'] = coins.is_valid()
        return render(request, 'home/home.html', context=context)
    return HttpResponse("خطا: تمام فیلدها باید پر شوند.", status=400)
    # # دریافت داده‌ها از URL (query parameters)
    # username = request.GET.get("username")
    # telegram_id = request.GET.get("telegram_id")
    # first_name = request.GET.get("first_name")
    # last_name = request.GET.get("last_name")

    # # بررسی اینکه آیا تمام اطلاعات موجود است یا خیر
    # if not all([username, telegram_id, first_name, last_name]):
    #     return HttpResponse("خطا: تمام فیلدها باید پر شوند.", status=400)

    # # بررسی اینکه آیا کاربر با این `telegram_id` قبلاً وجود دارد یا نه
    # existing_user = TelegramUser.objects.filter(telegram_id=telegram_id).first()

    # if existing_user:
    #     # وارد کردن کاربر به سیستم (login)
    #     login(request, existing_user)
    #     return render(request, 'home/home.html')

    # # ذخیره داده‌ها در دیتابیس و لاگین کاربر
    # user = TelegramUser(
    #     username=username,
    #     telegram_id=telegram_id,
    #     first_name=first_name,
    #     last_name=last_name
    # )
    # user.set_password("defaultpassword")  # اضافه کردن پسورد به صورت هش شده
    # user.save()

    # # ایجاد رکورد Coin برای کاربر جدید
    # user_coin = Coin(user=user, coin_amount=10**3)  # اختصاص مقدار اولیه 10 برای سکه‌ها
    # user_coin.save()

    # # وارد کردن کاربر به سیستم (login)
    # login(request, user)

    # # انتقال به صفحه دیگری پس از ذخیره موفقیت‌آمیز
    return render(request, 'home/home.html')


from datetime import timedelta
from django.utils.timezone import now
from django.http import JsonResponse
def coin_day(request, day):
    if request.method == 'POST':
        user = request.user
        coins = Coin.objects.get(user=user)
        if coins.is_valid():
            coins.coin_amount = 2**(day-1)
            coins.day += 1
            coins.next_day_time = now() + timedelta(days=1)
            return JsonResponse({'success': True, 'message': f'The coin increased.'})
        return JsonResponse({'success': False, 'message': f'Try the next day.'}, status=400)
    return JsonResponse({'success': False, 'message': f'Application must be by post only.'}, status=405)
        

