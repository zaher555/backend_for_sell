from rest_framework import serializers
from .models import *

class cateorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields='__all__'

class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model=color
        fields='__all__'

class productSerializer(serializers.ModelSerializer):
    color=colorSerializer(many=True)
    class Meta:
        model=product
        fields='__all__'
