from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'line1', 'city', 'country')
    search_fields = ('id', 'line1', 'city', 'country')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100