from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserNotification
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json


# @login_required
# def mark_as_read(request, notification_id):
#     user_notification = get_object_or_404(UserNotification, user=request.user, notification_id=notification_id)
#     if not user_notification.is_read:
#         # user_notification.is_read = True
#         # user_notification.read_at = timezone.now()
#         # user_notification.save()
#         user_notification.mark_as_read()
#     return JsonResponse({'status': 'success', 'message': 'Notification marked as read.'})


@csrf_exempt
def mark_notifications_as_read(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        notification_ids = data.get('ids', [])
        print(notification_ids)
        user_notifications = UserNotification.objects.filter(id__in=notification_ids)
        print(user_notifications)
        for user_notification in user_notifications:
            user_notification.mark_as_read()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'invalid request'}, status=400)
