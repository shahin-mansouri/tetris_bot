from django.shortcuts import render, redirect, HttpResponse
from django.utils.timezone import now
from .models import TetrisPlay

def tetris_play(request):
    user = request.user

    tetris_session = TetrisPlay.objects.filter(user=user, play_date=now().date()).first()

    if tetris_session:
        if tetris_session.duration >= 60:
            return HttpResponse("You have already played for 60 minutes today.", status=400)
    else:
        tetris_session = TetrisPlay(user=user, play_date=now().date(), duration=60, score=0)
        tetris_session.save()

    return render(request, 'tetris/game.html', {'tetris_session': tetris_session})