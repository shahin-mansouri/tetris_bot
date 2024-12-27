from django.urls import path
from .views import home, coin_day
from .views import coin_day_status


urlpatterns = [
    path("", home, name="home"),
    path('coin-increase/<int:day>/', coin_day, name='coin_increase'),
    path('coin-day-status/', coin_day_status, name='coin-day-status'),
]
