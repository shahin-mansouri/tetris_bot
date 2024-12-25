from django.contrib import admin
from .models import User, Token


# سفارشی‌سازی نمایش مدل User در پنل ادمین
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'first_name', 'last_name', 'is_active', 'invite_code', 'inviter', 'visit_site')  # ستون‌های قابل مشاهده
    list_filter = ('is_active',)  # فیلتر بر اساس فیلدهای خاص
    search_fields = ('username', 'telegram_id', 'first_name', 'last_name', 'invite_code')  # جستجو در فیلدهای خاص
    readonly_fields = ('invite_code',)  # فیلدهایی که فقط خواندنی هستند


# سفارشی‌سازی نمایش مدل Token در پنل ادمین
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'created_at', 'expires_at', 'is_used')  # ستون‌های قابل مشاهده
    list_filter = ('is_used', 'created_at')  # فیلتر بر اساس فیلدهای خاص
    search_fields = ('token', 'user__username', 'user__telegram_id')  # جستجو در فیلدهای خاص
    readonly_fields = ('created_at', 'expires_at')  # فیلدهایی که فقط خواندنی هستند
