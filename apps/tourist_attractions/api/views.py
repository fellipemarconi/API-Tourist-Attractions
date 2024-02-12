from rest_framework.viewsets import ModelViewSet
from ..models import TouristSpot
from .serializers import TouristSpotSerializer

class TouristAttractionViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer