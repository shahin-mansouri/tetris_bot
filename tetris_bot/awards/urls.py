from django.urls import path
from .views import AwardBlogListView


urlpatterns = [
    path("", AwardBlogListView.as_view(), name="awards")
]

