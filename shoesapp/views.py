from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .seriallizers import *
from core .customrespose import CustomResponse
from core .custompagination import CustomPagination
from rest_framework.permissions import IsAuthenticated

response = CustomResponse()


class ProductAiView(APIView):
    global response
    pagination_class = CustomPagination
   
    def get(self, request, pk=None):
    
        if pk:
            product_model = Product.objects.get(id=pk)
            if product_model:
                product_serializer = ProductSerializers(product_model)
                return Response(response.successResponse('data view', product_serializer.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_400_BAD_REQUEST)
            
        else: 
            product_model = Product.objects.all()
            
            if product_model:  
                paginator = self.pagination_class()
                paginated_queryset = paginator.paginate_queryset(product_model, request)
                
                product_serializer = ProductSerializers(paginated_queryset, many=True)
                
                response_data = {
                    'next': paginator.get_next_link(),
                    'previous': paginator.get_previous_link(),
                    'count': paginator.page.paginator.count,    
                    'data': product_serializer.data
                }
                
                return Response(response.successResponse('data view', response_data), status=status.HTTP_200_OK)
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
                
        
class CartApiView(APIView):
    
    global response
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    def get (self, request, pk=None):
        if pk:
            cart_obj = Cart.objects.get(id=pk)
            if cart_obj:
                cart_serializers = CartSerializers(cart_obj)
                return Response(response.successResponse('Data View', cart_serializers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
        else:
            cart_object = Cart.objects.all()
            
            if cart_object:
                paginator = self.pagination_class()
                paginated_queryset = paginator.paginate_queryset(cart_object, request)
                
                cart_serializer = CartSerializers(cart_object, many=True)
                response_data = {
                    'next': paginator.get_next_link(),
                    'previous': paginator.get_previous_link(),
                    'count': paginator.page.paginator.count,    
                    'data': cart_serializer.data
                }
                
                return Response(response.successResponse('Data View', response_data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
            
       
    def post(self, request):
        cart_serializers = CartSerializers(data=request.data)
        product_id = request.data.get('product_id')
        # user_id = request.user.id
        # print(user_id)

        if cart_serializers.is_valid():
            cart = cart_serializers.save()
            price = Product.objects.get(id=product_id)
            # print(price.product_name)

            product_cart_data = {
                'product_id': product_id,
                'product_name' : price.product_name,
                'cart_id': cart.id,
                'user_id': request.user.id, 
                'quantity': 1,  
                'price': price.product_price  
            }

            product_cart_serializer = Product_cartSerializers(data=product_cart_data)

            if product_cart_serializer.is_valid():
                product_cart_serializer.save()
                response_data = {
                    'cart_data': CartSerializers(cart).data,
                    'product_cart_data': Product_cartSerializers(product_cart_serializer.instance).data
                }

                return Response(response.successResponse('Data created', response_data), status=status.HTTP_201_CREATED)

            # If there are validation errors, you may want to log them for debugging purposes
            # print("Product Cart Validation Errors:", product_cart_serializer.errors)
            cart.delete()

        # If Cart serialization fails, return validation errors
        return Response(response.errorResponse('Validation error', cart_serializers.errors), status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk):
        
        try:
            cart_obj = Cart.objects.get(id=pk)
        except:
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND) 
        if cart_obj:
            cart_seriallizer = CartSerializers(cart_obj, data=request.data)
            if cart_seriallizer.is_valid():
                cart_seriallizer.save()
                return Response(response.successResponse('Data Saved', cart_seriallizer.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('Validation error', cart_seriallizer.errors),status=status.HTTP_400_BAD_REQUEST )
    
    def delete(self, request, pk):
        cart_obj = Cart.objects.get(id=pk)
        if cart_obj:
            cart_obj.delete()
            return Response(response.successResponse('Data deleted'), status=status.HTTP_204_NO_CONTENT)
        return Response(response.errorResponse('No Data found'), status=status.HTTP_404_NOT_FOUND)

class Product_cartApiView(APIView):
    global response
    
    def get(self, request, pk=None):
        if pk:
            product_cart_obj = Product_cart.objects.get(id=pk)
            if product_cart_obj:
                productcart_serillizers = Product_cartSerializers(product_cart_obj)
                if productcart_serillizers:
                    return Response(response.successResponse('data view', productcart_serillizers.data), status=status.HTTP_200_OK)
                return Response(response.errorResponse('no data found'), status=status.HTTP_404_NOT_FOUND)
        else:
            productcart = Product_cart.objects.all()
            product_cart_seriliser = Product_cartSerializers(productcart, many=True)
            if product_cart_seriliser:
                return Response(response.successResponse('data view', product_cart_seriliser.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('no data found'), status=status.HTTP_404_NOT_FOUND)
                
    def post(self, request):
        product_cart_serilizers = Product_cartSerializers(data=request.data)
        if product_cart_serilizers.is_valid():
            return Response(response.successResponse('Data Created', product_cart_serilizers.data), status=status.HTTP_201_CREATED)
        return Response(response.errorResponse('validataion error', product_cart_serilizers.errors), status=status.HTTP_400_BAD_REQUEST)
                           

    def put(self, request, pk):
        productcart_obj = Product_cart.objects.get(id=pk)
        if productcart_obj:
            productcart_serilizers = Product_cartSerializers(productcart_obj, data=request.data)
            if productcart_serilizers.is_valid():
                productcart_serilizers.save()
                return Response(response.successResponse('Data udated', productcart_serilizers.data), status=status.HTTP_200_OK)
            return Response(response.errorResponse('validation error', productcart_serilizers.errors), status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk):
        
        productcart_obj = Product_cart.objects.get(id=pk)
        if productcart_obj:
            productcart_obj.delete()
            return Response(response.successResponse('Data deleted'), status=status.HTTP_204_NO_CONTENT)
        return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)