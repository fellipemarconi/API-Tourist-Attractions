from rest_framework.viewsets import ModelViewSet
from ..models import TouristSpot
from .serializers import TouristSpotSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

from django.contrib.auth.models import User


class Pagination(LimitOffsetPagination):
    default_limit = 5

class TouristAttractionViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name', 'description', 'attractions']
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = Pagination
    lookup_field = "id"
    
    def get_queryset(self):
        queryset = TouristSpot.objects.filter(is_approved=True)
        return queryset
    
    @action(methods=['post'], detail=True)
    def set_has_attractions(self, request, id):
        attractions = request.data['ids']
        
        spot = TouristSpot.objects.get(id=id)
        spot.attractions.set(attractions)
        
        serializer = self.get_serializer(instance=spot)
        spot.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = Pagination
    
    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user.username) # type:ignore
        return queryset