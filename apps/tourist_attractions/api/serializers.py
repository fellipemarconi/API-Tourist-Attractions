from rest_framework import serializers
from ..models import TouristSpot
from ...attractions.api.serializers import AttractionSerializer
from ...address.api.serializers import AddressSerializer
from ...comments_reviews.api.serializers import CommentSerializer


class TouristSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = (
                'id', 'is_approved', 'name',
                'description', 'attractions','comment',
                'address', 'cover'
            )
        
    attractions = AttractionSerializer(many=True)
    address = AddressSerializer()
    comment = CommentSerializer(many=True)