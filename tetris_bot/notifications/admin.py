from django.contrib import admin
from django.utils.html import format_html
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'timestamp', 'is_read', 'get_time_ago', 'view_on_site')
    
    list_filter = ('is_read', 'timestamp', 'title')

    search_fields = ('title', 'description')

    list_editable = ('is_read',)

    def get_time_ago(self, obj):
        return obj.get_time_ago()
    get_time_ago.short_description = 'Time Ago'

    def view_on_site(self, obj):
        return format_html('<a href="/notifications/{}/" target="_blank">View</a>', obj.id)
    view_on_site.short_description = 'View On Site'

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'is_read')
        }),

    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_read=False)
    
    def description_preview(self, obj):
        return f"{obj.description[:50]}..." if len(obj.description) > 50 else obj.description
    description_preview.short_description = 'Description Preview'

    class Media:
        css = {
            'all': ('notifications/css/admin.css',)
        }
        js = ('notifications/js/admin.js',)
admin.site.register(Notification, NotificationAdmin)
