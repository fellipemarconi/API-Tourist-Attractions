from rest_framework.viewsets import ModelViewSet
from ..models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)