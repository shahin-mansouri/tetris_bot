from django.urls import path
from .views import  mark_notifications_as_read # , mark_as_read

urlpatterns = [
    # path('notifications/mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
    path('mark_notifications_as_read/', mark_notifications_as_read, name='mark_notifications_as_read'),
]
