from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from accounts.models import TelegramUser
from .models import Coin
from notifications.models import Notification, UserNotification
from youtube_auth.models import Youtube


def home(request):
    if request.user.is_authenticated:
        context = dict()
        user = request.user

        # اطلاعات مربوط به کوین‌ها
        coins, create = Coin.objects.get_or_create(user=user)
        context['coins'] = coins
        context['day'] = coins.day
        if coins.next_day_time is not None:
            context['next_day'] = coins.is_valid()

        # اطلاعات مربوط به نوتیفیکیشن‌ها
        notifications = UserNotification.objects.filter(user=user)
        context['user_notifications'] = notifications
        context['unread_notif'] = len([notification for notification in notifications if not notification.is_read])

        # بررسی لاگین بودن کاربر در Google و وضعیت سابسکرایب
        youtube_subscription = Youtube.objects.filter(user=user).first()
        context['youtube_subscription'] = youtube_subscription

        # بررسی پارامتر create
        create_param = request.GET.get('create')
        if create_param == 'true':  # مقایسه با رشته 'true'
            context['create'] = True

        return render(request, 'home/home.html', context=context)
    return HttpResponse("خطا: تمام فیلدها باید پر شوند.", status=400)


from datetime import timedelta
from django.utils.timezone import now
from django.http import JsonResponse
def coin_day(request, day):
    if request.method == 'POST':
        user = request.user
        coins = Coin.objects.get(user=user)
        if coins.is_valid():
            coins.coin_amount += (2**(day-1))*1000
            coins.day += 1
            coins.day = coins.day%5
            if not coins.day:
                coins.day = 1
            coins.next_day_time = now() + timedelta(days=1)
            coins.save()
            print('asdfasdfs')
            return JsonResponse({'success': True, 'message': 'The coin increased.', 'coin_amount': coins.coin_amount})
        return JsonResponse({'success': False, 'message': f'Try the next day.'}, status=400)
    return JsonResponse({'success': False, 'message': f'Application must be by post only.'}, status=405)
        

def coin_day_status(request):
    user = request.user
    coins = Coin.objects.get(user=user)
    return JsonResponse({'current_day': coins.day, 'next_day_time': coins.next_day_time })

