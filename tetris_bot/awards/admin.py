from django.contrib import admin
from .models import AwardBlog
from django.utils.safestring import mark_safe


@admin.register(AwardBlog)
class AwardBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'short_description', 'image_preview')
    search_fields = ('title', 'author', 'description')
    list_filter = ('date', 'author')
    fields = ('title', 'author', 'date', 'image', 'description')
    readonly_fields = ('image_preview',)

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description

    short_description.short_description = "Short Description"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 100px; max-height: 100px;">')
        return "No image available"
    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"
