from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from import_export.admin import ImportExportModelAdmin

from .models import (
    Clients,
    Services,
    People,
    PortfolioCategory,
    Portfolio,
    PortfolioImages,
    Team,
    Pricing,
    Extra
)

# Register your models here.

@admin.register(Clients)
class ClientsModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['fullname',]
    search_fields = ['fullname']


@admin.register(Services)
class ServicesModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['title',]
    search_fields = ['title']


@admin.register(People)
class PeopleModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['fullname', 'position']
    search_fields = ['fullname', 'position']
    list_filter = ['position']


@admin.register(PortfolioCategory)
class PortfolioCategoryModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name',]
    search_fields = ['name']


@admin.register(PortfolioImages)
class PortfolioImagesModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name']


@admin.register(Portfolio)
class ClientsModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['title', 'project_url', 'category']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'category']



@admin.register(Team)
class TeamModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['fullname', 'position']
    list_filter = ['position']
    search_fields = ['fullname', 'position']


@admin.register(Pricing)
class PricingModelAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']

@admin.register(Extra)
class ExtraModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass


