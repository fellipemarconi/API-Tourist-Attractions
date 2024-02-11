from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'minimal_age')
    search_fields = ('id', 'name', 'minimal_age')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100