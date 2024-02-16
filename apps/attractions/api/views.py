from rest_framework.viewsets import ModelViewSet
from ..models import Attraction
from .serializers import AttractionSerializer

class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer