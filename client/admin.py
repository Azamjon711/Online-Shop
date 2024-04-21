from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Address, City, Country, Customer

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ("name", )
    list_display_links = ("name", )


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ("name", )
    list_display_links = ("name", )


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ("name", )
    list_display_links = ("name", )


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ("first_name", "last_name", "zipcode", "phone_umber", "email", "address", "city", "country",)
    list_display_links = ("first_name", "last_name", "zipcode", "phone_umber", "email", "address", "city", "country",)
    search_fields = ("first_name", "last_name",)
