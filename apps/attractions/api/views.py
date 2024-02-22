from rest_framework.viewsets import ModelViewSet
from ..models import Attraction
from .serializers import AttractionSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name', 'description', 'minimal_age']