from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.utils.timezone import now
from .models import TetrisPlay
from home.models import Coin
from django.http import JsonResponse


def tetris_play(request):
    user = request.user

    tetris_session = TetrisPlay.objects.filter(user=user, play_date=now().date()).first()
    if tetris_session is not None:
        timer = 300 - tetris_session.duration
    else:
        tetris_session = TetrisPlay.objects.create(user=user, play_date=now().date())
        timer = 300 - tetris_session.duration
    timer = f"{timer // 60}:{timer % 60:02}"

    if tetris_session:
        if tetris_session.duration >= 300:
            return HttpResponse("You have already played for 5 minutes today.", status=400)
    else:


        pass

    return render(request, 'tetris/game.html', {'tetris_session': tetris_session, 'timer': timer})




@csrf_exempt
@login_required
def tetris_time_play(request, score, time):
    if request.method == 'POST':
        try:
            user = request.user
            # Validate time and score
            if not isinstance(score, int) or not isinstance(time, int):
                return JsonResponse({'success': False, 'error': 'Invalid parameters.'}, status=400)

            # Get or create TetrisPlay record
            game, created = TetrisPlay.objects.get_or_create(user=user)
            coin = Coin.objects.get(user=user)

            # Update records
            game.duration += time
            game.save()

            coin.coin_amount += score
            coin.save()

            return JsonResponse({
                'success': True,
                'message': 'Game data updated successfully.',
                'game_duration': game.duration,
                'coin_amount': coin.coin_amount
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)
