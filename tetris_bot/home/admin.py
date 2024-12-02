from django.contrib import admin
from .models import Coin

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    # فیلدهایی که می‌خواهیم در پنل مدیریت نمایش داده شوند
    list_display = ('user', 'coin_amount')  # نمایش نام کاربر و تعداد سکه‌ها
    
    # فیلدهایی که می‌خواهیم قابل جستجو باشند
    search_fields = ('user__username',)  # جستجو بر اساس نام کاربری
    list_filter = ('coin_amount',)  # فیلتر بر اساس تعداد سکه‌ها
