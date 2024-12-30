from django.shortcuts import render
from telegram_bot.models import User
from django.contrib.auth.decorators import login_required
from telegram_bot.models import User
from accounts.models import TelegramUser
from home.models import Coin


@login_required
def invitionView(request):
    context = dict()
    user = request.user

    current_user = Coin.objects.get(user=user) 
    context['current_user'] = current_user

    if user.invite_code is not None:
        context['invite_code'] = user.invite_code
        return render(request, 'invition/earn.html', context)
    
    invite_code = User.objects.get(telegram_id=user.telegram_id).invite_code
    user.invite_code = invite_code
    context['invite_code'] = invite_code

    invited_users = User.objects.filter(inviter__telegram_id=user.telegram_id)
    telegram_ids = list(invited_users.values_list('telegram_id', flat=True))
    
    similar_users = TelegramUser.objects.filter(telegram_id__in=telegram_ids)
    
    s_u_coins = Coin.objects.filter(user__in=similar_users)
    context['invitees5'] = s_u_coins[:5]
    context['invitees'] = s_u_coins

    return render(request, 'invition/earn.html', context)

