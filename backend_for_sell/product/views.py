from django.http import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
# Create your views here.


#Categories API
class categories_list(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self,request):
            if request.method == 'GET':
                    categories=category.objects.all()
                    serializer=cateorySerializer(categories,many=True)
                    return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
            if request.method == 'POST':
                serializer=cateorySerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class one_category(APIView):
    # permission_classes=[IsAuthenticated]
    def category_object(self,pk):
        try: return category.objects.get(id=pk)
        except category.DoesNotExist:
               raise Http404
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
    
#Products API
# @method_decorator(cache_page(60 * 60 * 2))
# @method_decorator(cache_page(60 * 60 * 2), name='get')
class productsList(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        if self.request.method == 'GET':
            products=product.objects.all()
            serializer=productSerializer(products,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        if request.method == 'POST':
            serializer=productSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class one_product(APIView):
    # permission_classes=[IsAuthenticated]
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
    
#Colors API
class colors_list(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        if request.method == 'GET':
            colors=color.objects.all()
            serializer=colorSerializer(colors,many=True)
            return Response(serializer.data,status=status.HTTP_302_FOUND)
    def post(self,request):
        if request.method == 'POST':
            serializer=colorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class one_color(APIView):
    # permission_classes=[IsAuthenticated]
    def color_object(self,pk):
        try: return color.objects.get(id=pk)
        except color.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        if request.method == 'GET':
            color=self.color_object(pk)
            serializer=colorSerializer(color)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        if request.method == 'PUT':
            color=self.color_object(pk)
            serializer=colorSerializer(color,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        if request.method == 'DELETE':
            color=self.color_object(pk)
            color.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# customer_product_rate API 
# class customer_rateView(APIView):
#     # permission_classes=[IsAuthenticated]
#     def get(self, request,product_id,customer_id):
#         ratings = customer_rate.objects.all()
#         serializer = customerRateSerializer(ratings, many=True)
#         return Response(serializer.data)

#     def post(self, request,product_id,customer_id):
#         data = request.data.copy()
#         data['customer'] = customer_id
#         data['product'] = product_id
#         serializer = customerRateSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)