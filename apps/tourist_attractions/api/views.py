from rest_framework.viewsets import ModelViewSet
from ..models import TouristSpot
from .serializers import TouristSpotSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

class TouristAttractionViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['name', 'description', 'attractions']
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    
    def get_queryset(self):
        queryset = TouristSpot.objects.filter(is_approved=True)
        return queryset
    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user.username) # type:ignore
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)