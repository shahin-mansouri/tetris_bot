from django .urls import path
from .views import tetris_play


urlpatterns = [
    path('lunch-game/', tetris_play, name='lunch_game')
]

