from django.urls import path
from .views import home, coin_day


urlpatterns = [
    path("", home, name="home"),
    path('coin-increase/<int:day>/', coin_day, name='coin_increase'),
]
