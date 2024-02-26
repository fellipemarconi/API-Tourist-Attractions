from rest_framework import serializers
from ..models import TouristSpot
from ...attractions.api.serializers import AttractionSerializer
from ...address.api.serializers import AddressSerializer
from ...comments_reviews.api.serializers import CommentSerializer

from django.core import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
        user = User(**validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        
        user.save()
        return user
    
    def validate_email(self, value):
        email = value
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already registered', code='invalid')
        
        return email
    
    def validate_password(self, data):
        try:
            password_validation.validate_password(password=data, user=data)
            
        except exceptions.ValidationError as e:
            errors = list(e.messages)
            raise serializers.ValidationError(errors)
        
        return data
    
class TouristSpotSerializer(serializers.ModelSerializer):
    attractions = AttractionSerializer(many=True)
    address = AddressSerializer()
    comment = CommentSerializer()
    
    
    class Meta:
        model = TouristSpot
        fields = (
                'id', 'is_approved', 'name',
                'description', 'attractions','comment',
                'address', 'cover'
            )
    