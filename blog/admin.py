from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from import_export.admin import ImportExportModelAdmin

from .models import (
    Category,
    Blog,
    BlogImages,
)
# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name']


@admin.register(BlogImages)
class BlogImages(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name']

@admin.register(Blog)
class BlogModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['title', 'slug', 'author', 'comments', 'category']
    list_filter = ['title', 'author', 'category']
    search_fields = ['category', 'author', 'title']
