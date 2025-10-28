from django.forms import EmailField
from rest_framework import serializers
from .models import *

class permissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=permission
        fields='__all__'

class customerSerializer(serializers.ModelSerializer):
    permission=permissionSerializer(many=True)
    # email = serializers.EmailField()    
    class Meta:
        model=customer
        fields='__all__'
