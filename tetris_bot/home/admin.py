from django.contrib import admin
from .models import Coin

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('user', 'coin_amount')
    
    search_fields = ('user__username',)
    list_filter = ('coin_amount',)


admin.site.site_header = "Tetris Game Admin"
admin.site.site_title = "Tetris Game Admin Panel"
admin.site.index_title = "Welcome to Tetris Game Admin"
