from rest_framework import routers
from apps.tourist_attractions.api.views import TouristAttractionViewSet
from apps.attractions.api.views import AttractionsViewSet
from apps.address.api.views import AddressViewSet


router = routers.DefaultRouter()
router.register(r'touristattractions', TouristAttractionViewSet, basename='tourist_attractions')
router.register(r'attractions', AttractionsViewSet, basename='attractions')
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = router.urls