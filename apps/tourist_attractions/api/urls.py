from rest_framework import routers
from apps.tourist_attractions.api.views import TouristAttractionViewSet
from apps.attractions.api.views import AttractionsViewSet

router = routers.DefaultRouter()
router.register(r'touristattractions', TouristAttractionViewSet, basename='tourist_attractions')
router.register(r'attractions', AttractionsViewSet, basename='attractions')

urlpatterns = router.urls