from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Type, Product


@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "description", "price", "type", )
    list_display_links = ("name", "description", "price", "type", )
    search_fields = ("name", "description",)
    list_filter = ("name", "price", "type",)

    def description_length(self, obj):
        return obj.description[:15]








