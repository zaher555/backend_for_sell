from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

#Customers API
class customers_list(APIView):
    def get(self,request):
        if request.method == 'GET':
            customers=customer.objects.all()
            serializer=customerSerializer(customers,many=True)
            return Response(serializer.data,status=status.HTTP_302_FOUND)
    def post(self,request):
        if request.method == 'POST':
            serializer=customerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
class one_customer(APIView):
    def customer_object(self,pk):
        try: return customer.objects.get(id=pk)
        except customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        if request.method == 'GET':
            customer=self.customer_object(pk)
            serializer=customerSerializer(customer)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        if request.method == 'PUT':
            customer=self.customer_object(pk)
            serializer=customerSerializer(customer,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        if request.method == 'DELETE':
            customer=self.customer_object(pk)
            customer.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    




