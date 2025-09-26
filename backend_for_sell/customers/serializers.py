from rest_framework import serializers
from .models import *
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields='__all__'