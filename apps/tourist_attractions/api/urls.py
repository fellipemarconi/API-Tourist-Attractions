from rest_framework import routers
from apps.tourist_attractions.api import views

router = routers.DefaultRouter()
router.register(r'touristattractions', views.TouristAttractionViewSet, basename='tourist_attractions')

urlpatterns = router.urls