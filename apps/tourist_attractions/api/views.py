from rest_framework.viewsets import ModelViewSet
from ..models import TouristSpot
from .serializers import TouristSpotSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class TouristAttractionViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name', 'description', 'attractions']
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    
    def get_queryset(self):
        queryset = TouristSpot.objects.filter(is_approved=True)
        return queryset