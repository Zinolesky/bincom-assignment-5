from django.contrib import admin
from .models import Category, MediaItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'category', 'views_count', 'uploaded_at')
    list_filter = ('media_type', 'category', 'uploaded_at')
    search_fields = ('title', 'description')
    readonly_fields = ('views_count', 'uploaded_at')
