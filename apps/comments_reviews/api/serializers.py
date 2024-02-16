from rest_framework import serializers
from ..models import Comment, Review


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'date',
                  'is_approved', 'review'
                  )
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'note')
