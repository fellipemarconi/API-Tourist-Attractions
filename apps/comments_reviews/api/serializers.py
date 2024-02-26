from rest_framework import serializers
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'date', 'review', 'tourist_spot')
    
    user = serializers.CharField(source="user.username", read_only=True)
    
    
