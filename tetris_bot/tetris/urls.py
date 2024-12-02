from django .urls import path
from .views import *


urlpatterns = [
    path('lunch-game/', tetris, name='lunch_game')
]

