from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .seriallizers import *
from core .customrespose import CustomResponse

response = CustomResponse()


class ProductAiView(APIView):
    global response
    def get(self, request, pk=None):
        if pk:
            produt_model = Product.objects.get(id=pk)
            if produt_model:
                product_serializers = ProductSerializers(produt_model)
                return Response(response.successResponse('data view', product_serializers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('NO-data found'), status=status.HTTP_400_BAD_REQUEST)
            
        else: 
            product_model= Product.objects.all()
            product_serializers = ProductSerializers(product_model, many=True)
            if product_serializers:
                return Response(response.successResponse('data view', product_serializers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request): 
        product_serilizers = ProductSerializers(data=request.data)
        if product_serilizers.is_valid():
            product_serilizers.save()
            return Response(response.successResponse('Data Created', product_serilizers.data), status=status.HTTP_201_CREATED)
        return Response(response.errorResponse('validation errors', product_serilizers.errors), status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk): 
        product_obj = Product.objects.get(id=pk)
        if product_obj:
            product_obj.delete()
            return Response(response.successResponse('Data Deleted'), status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        product_obj = Product.objects.get(id=pk)
        if product_obj:
            product_serilizers = ProductSerializers(product_obj, data=request.data)
            if product_serilizers.is_valid():
                product_serilizers.save()
                return Response(response.successResponse('Data Updated', product_serilizers.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
                
        
 
       
   
