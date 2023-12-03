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
                
        
class BrandApiView(APIView):
    
    global response
    
    def get(self, request, pk=None):
        
        if pk:
            brand_obj = Brand.objects.get(id=pk)
            brand_seriallizers = BrandSerializers(brand_obj)
            if brand_seriallizers:
                return Response(response.successResponse('Data View', brand_seriallizers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
        
        else:
            brand_obj = Brand.objects.all()
            brand_seriallizers = BrandSerializers(brand_obj, many=True)
            if brand_seriallizers:
                return Response(response.successResponse('Data View', brand_seriallizers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        brand_serializer = BrandSerializers(data=request.data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response(response.successResponse('Data Created', brand_serializer.data), status=status.HTTP_201_CREATED)
        return Response(response.errorResponse('validation errors', brand_serializer.errors), status=status.HTTP_400_BAD_REQUEST)
                       
    def put(self, request, pk):
        
        brand_obj = Brand.objects.get(id=pk)
        if brand_obj:
            brand_serializer = BrandSerializers(brand_obj, data=request.data)
            if brand_serializer.is_valid():
                brand_serializer.save()
                return Response(response.successResponse('Data Updated', brand_serializer.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('Validation error', brand_serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
    
    
    def delete(self, request, pk):
        
        brand_obj = Brand.objects.get(id=pk)
        if brand_obj:
            brand_obj.delete()
            return Response(response.successResponse('Data Deleted'), status=status.HTTP_204_NO_CONTENT)
        return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)


class ProductBrandApiview(APIView):
    global response
    
    def get(self, request, pk=None):
        
        if pk:
            brand_obj = Product_Brand.objects.get(id=pk)
            productbrand_seriallizers = Product_BrandSerializers(brand_obj)
            if productbrand_seriallizers:
                return Response(response.successResponse('Data View', productbrand_seriallizers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
        
        else:
            product_brand_obj = Product_Brand.objects.all()
            product_brand_seriallizers = Product_BrandSerializers(product_brand_obj, many=True)
            if product_brand_seriallizers:
                return Response(response.successResponse('Data View', product_brand_seriallizers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        product_brand_serializer = Product_BrandSerializers(data=request.data)
        if product_brand_serializer.is_valid():
            product_brand_serializer.save()
            return Response(response.successResponse('Data Created', product_brand_serializer.data), status=status.HTTP_201_CREATED)
        return Response(response.errorResponse('validation errors', product_brand_serializer.errors), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        product_brand_obj = Product_Brand.objects.get(id=pk)
        if product_brand_obj:
            product_brand_serializer = Product_BrandSerializers(product_brand_obj, data=request.data)
            if product_brand_serializer.is_valid():
                product_brand_serializer.save()
                return Response(response.successResponse('Data Updated', product_brand_serializer.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('validation error', product_brand_serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        
        product_brand = Product_Brand.objects.get(id=pk)
        if product_brand:
            product_brand.delete()
            return Response(response.successResponse('Data Deleted'),status=status.HTTP_200_OK)
        return Response(response.errorResponse('No data found'),status= status.HTTP_404_NOT_FOUND)  
       

class ProductImageApiview(APIView):
    global response
    
    def get(self, request, pk=None):
        
        if pk:
            prdimagre_obj = ProductImage.objects.get(id=pk)
            prodimg_seriallizers = ProductImageSerializers(prdimagre_obj, many=True)
            if prodimg_seriallizers:
                return Response(response.successResponse('Data View', prodimg_seriallizers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
        
        else:
            prdimagre_obj = ProductImage.objects.all()
            product_img_seriallizers = ProductImageSerializers(prdimagre_obj, many=True)
            if product_img_seriallizers:
                return Response(response.successResponse('Data View', product_img_seriallizers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        product_img_serializer = ProductImageSerializers(data=request.data)
        if product_img_serializer.is_valid():
            product_img_serializer.save()
            return Response(response.successResponse('Data Created', product_img_serializer.data), status=status.HTTP_201_CREATED)
        return Response(response.errorResponse('validation errors', product_img_serializer.errors), status=status.HTTP_400_BAD_REQUEST)     
