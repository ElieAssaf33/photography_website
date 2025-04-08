from django.contrib import admin
from .models import Photos

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'photo']
    list_filter = ['category']
    search_fields = ['title', 'category']
