from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#Products API
class products_list(APIView):
    def get(self,request):
        if request.method == 'GET':
            products=product.objects.all()
            serializer=productSerializer(products,many=True)
            return Response(serializer.data,status=status.HTTP_302_FOUND)
    def post(self,request):
        if request.method == 'POST':
            serializer=productSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
class one_product(APIView):
    def product_object(self,pk):
        try: return product.objects.get(id=pk)
        except product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        if request.method == 'GET':
            product=self.product_object(pk)
            serializer=productSerializer(product)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        if request.method == 'PUT':
            product=self.product_object(pk)
            serializer=productSerializer(product,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        if request.method == 'DELETE':
            product=self.product_object(pk)
            product.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
#Categories API
class categories_list(APIView):
    def get(self,request):
        if request.method == 'GET':
            categories=category.objects.all()
            serializer=cateorySerializer(categories,many=True)
            return Response(serializer.data,status=status.HTTP_302_FOUND)
    def post(self,request):
        if request.method == 'POST':
            serializer=cateorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
class one_category(APIView):
    def category_object(self,pk):
        try: return category.objects.get(id=pk)
        except category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        if request.method == 'GET':
            category=self.category_object(pk)
            serializer=cateorySerializer(category)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        if request.method == 'PUT':
            category=self.category_object(pk)
            serializer=cateorySerializer(category,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        if request.method == 'DELETE':
            category=self.category_object(pk)
            category.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)




