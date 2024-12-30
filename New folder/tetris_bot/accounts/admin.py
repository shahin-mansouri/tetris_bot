from django.contrib import admin
from .models import TelegramUser


# استفاده از دکوریتور @admin.register برای ثبت مدل TelegramUser در پنل مدیریت
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    # فیلدهایی که می‌خواهیم در پنل مدیریت نمایش داده شوند
    list_display = ('username', 'telegram_id', 'first_name', 'last_name', 'id')
    
    # فیلدهایی که می‌خواهیم قابل جستجو باشند
    search_fields = ('username', 'first_name', 'last_name', 'telegram_id')
    
    # فیلدهایی که می‌خواهیم قابل فیلتر باشند
    list_filter = ('first_name', 'last_name')
    
    # حذف فیلدهای groups و user_permissions از فرم مدیریت
    exclude = ('groups', 'user_permissions')

# استفاده از دکوریتور @admin.register برای ثبت مدل Coin در پنل مدیریت
