from rest_framework import routers
from apps.tourist_attractions.api.views import TouristAttractionViewSet, UserViewSet
from apps.attractions.api.views import AttractionViewSet
from apps.address.api.views import AddressViewSet
from apps.comments_reviews.api.views import CommentViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'touristattractions', TouristAttractionViewSet, basename='tourist_attractions')
router.register(r'attractions', AttractionViewSet, basename='attractions')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls