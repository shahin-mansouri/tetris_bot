from django.urls import path
from . import views

urlpatterns = [
    path('login-with-google/', views.login_with_google, name='login_with_google'),
    path('callback/', views.callback, name='callback'),
    path('check-subscription-status/', views.check_subscription_status, name='check_subscription_status'),
]