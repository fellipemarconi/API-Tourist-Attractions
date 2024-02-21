from django.urls import path, include


urlpatterns = [
    path('', include('apps.tourist_attractions.api.urls')),
]
