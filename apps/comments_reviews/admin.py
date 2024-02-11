from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'review', 'is_approved')
    search_fields = ('id', 'user')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100
    
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'note')
    search_fields = ('id', 'user')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100