from django.urls import path
from .views import tetris_play, tetris_time_play

urlpatterns = [
    path('lunch-game/', tetris_play, name='lunch_game'),
    path('end_game/<int:score>/<int:time>/', tetris_time_play, name='end_game'), #game/end_game/10/
]
