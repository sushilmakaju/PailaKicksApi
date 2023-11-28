
from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serilizers import *
from core.customrespose import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

response = CustomResponse()
# Create your views here.
class LoginApi(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        auth = authenticate(username=email, password=password)
        
        if auth:
            token, _ = Token.objects.get_or_create(user=auth)
            return Response(response.successResponse("You have logged in successfully", {"token": token.key}), status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserAPiView(APIView):
        
    def get(self, request, pk=None):
        if pk is None:       
            user_obj = User.objects.all()
            user_serializer = GetUsersSeriallizers(user_obj, many = True)   
            response_data = {
                'data' : user_serializer.data
            }     
            if user_obj:
                return Response(response.successResponse("data view", response_data), status=status.HTTP_200_OK)
            else:
                return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
        else:
            user_obj = User.objects.get(id=pk)
            if user_obj:
                user_serilizer = GetUsersSeriallizers(user_obj)
                return Response(response.successResponse('data view', user_serilizer.data), status=status.HTTP_200_OK)
            else: 
                return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
   
    
    def post(self, request):       
        user_serializer = UsersSeriallizers(data=request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            response_data = {
                'data' : user_serializer.data
            }
            return Response(response.successResponse("data view", response_data), status=status.HTTP_201_CREATED)           
        else:
            return Response(response.errorResponse("HTTP_400_BAD_REQUEST", user_serializer.errors), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):        
        try:
            user_obj = User.objects.get(id=pk)
        except:
            return Response(response.errorResponse("No Data Found"),status=status.HTTP_404_NOT_FOUND)
        user_serializer = UsersSeriallizers(user_obj, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(response.successResponse("Data Updated", user_serializer.errors), status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        try:
            user_obj = User.objects.get(id=pk)
        except:
            return Response(response.errorResponse('No data found'), status=status.HTTP_404_NOT_FOUND)
        if user_obj:
            user_obj.delete()
            return Response(response.successResponse('Data Deleted'), status=status.HTTP_200_OK)
        
class AddressApiView(APIView):
    
    serializer = AddressSerialzers
    
    def get(self, request):
        address_obj = Address.objects.all()
        address_serializer = self.serializer(address_obj, many=True)
        if address_obj:
            return Response(response.successResponse('data view',address_serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse('No Data Found'), status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        address_serialier = self.serializer(data=request.data)
        if address_serialier.is_valid():
            address_serialier.save()
            return Response(response.successResponse('data created',address_serialier.data), status=status.HTTP_201_CREATED)
        return Response(response.errorResponse('validation error',address_serialier.errors),status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        address_obj = Address.objects.get(id = pk)
        if address_obj:
            address_obj.delete()
            return Response(response.successResponse('data deleted'),status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse('No data found'),status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        try:
            address_obj = Address.objects.get(id=pk)
        except:
            return Response(response.errorResponse('No data found'),status=status.HTTP_404_NOT_FOUND)
        adress_serialier = self.serializer(address_obj, data=request.data)
        if adress_serialier.is_valid():
            adress_serialier.save()
            return Response(response.successResponse('data updated',adress_serialier.data), status=status.HTTP_201_CREATED)
        else:
            return Response(response.errorResponse('validation error',adress_serialier.errors),status=status.HTTP_400_BAD_REQUEST)
            
class LogoutApiView(APIView):

    def get(self, request):
        user = request
        logout(user)
        response = CustomResponse()
        return Response(response.successResponse("You have successfully Logged Out"), status=status.HTTP_200_OK)