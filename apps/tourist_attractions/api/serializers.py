from rest_framework import serializers
from ..models import TouristSpot
from ...attractions.api.serializers import AttractionSerializer
from ...attractions.models import Attraction
from ...address.api.serializers import AddressSerializer
from ...address.models import Address
from ...comments_reviews.api.serializers import CommentSerializer
from ...comments_reviews.models import Comment

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
    
    def create_attractions(self, attractions, tourist_spot):
        for attraction in attractions:
            spot = Attraction.objects.create(**attraction)
            tourist_spot.attractions.add(spot)
    
    def create_address(self, address, tourist_spot):
        addrs = Address.objects.create(**address)
        tourist_spot.address = addrs
        
    def create_comment(self, comment, tourist_spot):
        user = self.context['request'].user
        comnt = Comment.objects.create(**comment, user=user, tourist_spot=tourist_spot)
        
        tourist_spot.comment = comnt
    
    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']
        
        address = validated_data['address']
        del validated_data['address']
        
        comment = validated_data['comment']
        del validated_data['comment']
        
        tourist_spot = TouristSpot.objects.create(**validated_data)
        
        self.create_attractions(attractions, tourist_spot)
        self.create_address(address, tourist_spot)
        self.create_comment(comment, tourist_spot)
        
        tourist_spot.save()
        return tourist_spot
