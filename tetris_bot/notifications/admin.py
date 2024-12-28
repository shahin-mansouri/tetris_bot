# myapp/admin.py
from django.contrib import admin
from .models import Notification, UserNotification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'get_time_ago')
    search_fields = ('title', 'description')
    list_filter = ('timestamp',)

    def get_time_ago(self, obj):
        return obj.get_time_ago()
    get_time_ago.short_description = 'Time Ago'

class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification', 'is_read', 'read_at', 'notification_time')
    search_fields = ('user__username', 'user__email', 'notification__title', 'notification__description')
    list_filter = ('is_read', 'read_at', 'notification__timestamp', 'user__date_joined', 'user__is_active')
    raw_id_fields = ('user', 'notification')
    date_hierarchy = 'read_at'
    ordering = ('-read_at',)

    def notification_time(self, obj):
        return obj.notification.timestamp
    notification_time.short_description = 'Notification Time'
    notification_time.admin_order_field = 'notification__timestamp'

admin.site.register(Notification, NotificationAdmin)
admin.site.register(UserNotification, UserNotificationAdmin)
