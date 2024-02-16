from rest_framework.viewsets import ModelViewSet
from ..models import TouristSpot
from .serializers import TouristSpotSerializer

class TouristAttractionViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    
    def get_queryset(self):
        qs = TouristSpot.objects.filter(is_approved=True)
        return qs