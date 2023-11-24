
from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serilizers import *
# Create your views here.
class LoginApi(APIView):
    
    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        auth = authenticate(username = email, password=password)
        
        if auth:
            return Response('Login sucessfull', status= status.HTTP_200_OK)
        return Response('Validation Error', status=status.HTTP_400_BAD_REQUEST)
    
class UserAPi(APIView):
        
    def get(self, request):       
        user_obj = User.objects.all()
        user_serializer = GetUsersSeriallizers(user_obj, many = True)        
        if user_obj:
            return Response(user_serializer.data)
        else:
            return Response('No data found')
   
    
    def post(self, request):       
        user_serializer = UsersSeriallizers(data=request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(data=user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):        
        try:
            user_obj = User.objects.get(id=pk)
        except:
            return Response('Data Not Found!')
        user_serializer = UsersSeriallizers(user_obj, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors)
    
    def delete(self, request, pk):
        try:
            user_obj = User.objects.all()
        except:
            return Response('No data found')
        if user_obj:
            user_obj.delete()
            return Response ('Data Deleted')