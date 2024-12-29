from django.contrib import admin
from .models import TetrisPlay

@admin.register(TetrisPlay)
class TetrisPlayAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'play_date', 'duration', 'score', 'is_today')
    list_display_links = ('id', 'user')
    list_editable = ('duration', 'score')
    list_filter = ('play_date', 'user')
    search_fields = ('user__username', 'user__telegram_id')
    ordering = ('-play_date', 'user', '-score')
    date_hierarchy = 'play_date'
    readonly_fields = ('play_date',)
    fields = ('user', 'play_date', 'duration', 'score')

    def is_today(self, obj):
        from django.utils.timezone import now
        return obj.play_date == now().date()

    is_today.boolean = True
    is_today.short_description = "Is Today?"
