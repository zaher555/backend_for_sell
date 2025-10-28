from rest_framework import serializers
from .models import *
# from customer.serializers import *

class cateorySerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=category
        fields=['id','title','productsNumber','products']

class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model=color
        fields='__all__'

class productSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField() 
    # color = serializers.StringRelatedField(many=True)
    class Meta:
        model=product
        fields='__all__'
        depth=1

# class customerRateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=customer_rate
#         fields = ['id', 'customer', 'product', 'rate']
