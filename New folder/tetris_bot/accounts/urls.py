from django.urls import path
from .views import ProfileView
from .views import logout


urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", logout, name='logout'),
]

