from django.urls import path
from .views import invitionView


urlpatterns = [
    path("", invitionView, name="invition")
]

