from django.urls import path, include

from .api import views

urlpatterns = [
    path('', include('apps.tourist_attractions.api.urls')),
]