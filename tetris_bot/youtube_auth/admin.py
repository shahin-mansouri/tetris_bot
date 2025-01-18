from django.contrib import admin
from .models import Youtube

class YoutubeAdmin(admin.ModelAdmin):
    # فیلدهایی که در لیست نمایش داده می‌شوند
    list_display = (
        'user', 
        'is_sub', 
        'channel_url', 
        'subscription_date', 
        'last_updated', 
        'is_active',
        'access_token',  # نمایش توکن دسترسی
        'refresh_token',  # نمایش توکن رفرش
        'token_expiry',   # نمایش تاریخ انقضای توکن
    )

    # فیلترهای قابل استفاده در پنل ادمین
    list_filter = (
        'is_sub', 
        'is_active',
    )

    # فیلدهای قابل جست‌وجو
    search_fields = (
        'user__username', 
        'channel_url',
    )

    # فیلدهای قابل ویرایش در لیست
    list_editable = (
        'is_sub', 
        'is_active',
    )

    # گروه‌بندی فیلدها در صفحه ویرایش
    fieldsets = (
        (None, {
            'fields': (
                'user', 
                'is_sub', 
                'channel_url', 
                'is_active',
                'access_token',  # اضافه کردن توکن دسترسی
                'refresh_token',  # اضافه کردن توکن رفرش
                'token_expiry',   # اضافه کردن تاریخ انقضای توکن
            )
        }),
    )

    # فیلدهای فقط خواندنی
    readonly_fields = (
        'last_updated', 
        'subscription_date',
        'access_token',  # توکن دسترسی فقط خواندنی
        'refresh_token',  # توکن رفرش فقط خواندنی
        'token_expiry',   # تاریخ انقضای توکن فقط خواندنی
    )

    # متدهای سفارشی برای نمایش فیلدها
    def subscription_date(self, obj):
        return obj.subscription_date
    subscription_date.admin_order_field = 'subscription_date' 
    subscription_date.short_description = 'Subscription Date'

    def last_updated(self, obj):
        return obj.last_updated
    last_updated.admin_order_field = 'last_updated' 
    last_updated.short_description = 'Last Updated'

    # محدود کردن دسترسی به سوپر یوزرها
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser 

# ثبت مدل Youtube با کلاس ادمین سفارشی
admin.site.register(Youtube, YoutubeAdmin)