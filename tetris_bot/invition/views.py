from django.shortcuts import render
from telegram_bot.models import User
from django.contrib.auth.decorators import login_required


@login_required
def invitionView(request):
    context = dict()
    user = request.user
    if user.invite_code is not None:
        context['invite_code'] = user.invite_code
        return render(request, 'invition/earn.html', context)
    invite_code = User.objects.get(telegram_id=user.telegram_id).invite_code
    user.invite_code = invite_code
    context['invite_code'] = invite_code
    return render(request, 'invition/earn.html', context)
