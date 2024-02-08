from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.TouristSpot)
class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_approved')
    search_fields = ('id', 'name')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100