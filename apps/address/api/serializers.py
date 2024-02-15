from rest_framework import serializers
from ..models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'line1', 'line2', 'city',
                  'state', 'country', 'latitude',
                  'longitude'
                  )