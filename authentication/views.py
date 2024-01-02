from rest_framework.permissions import AllowAny
from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import *
from .serilizers import *
from core.customrespose import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from core.custompagination import *


response = CustomResponse()
# Create your views here.
class LoginApi(GenericAPIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        auth = authenticate(username=email, password=password)
        
        if auth:
            token, _ = Token.objects.get_or_create(user=auth)
            user_id = auth.id
            response_data = {
                "success": True,  # Adding the status field for success
                "data": {
                    "user_id": user_id,
                    "token": token.key,
                    # Add other user-related data here
                },
            }
            return Response(response.successResponse("You have logged in successfully", response_data), status=status.HTTP_200_OK)
        
        response_data = {
            "success": False,  # Adding the status field for failure
            "data": {},  # You can provide additional error details if needed
            "message": 'Invalid credentials',
        }
        return Response(response.errorResponse(response_data), status=status.HTTP_401_UNAUTHORIZED)
    
class UserAPiView(GenericAPIView):
    filterset_fields = ['id', 'first_name','last_name', 'email', 'address']
    search_fields = ['first_name', 'last_name', 'email']
    permission_classes = [IsAuthenticated, AllowAny]
    pagination_class = CustomPagination()
    
    def get(self, request, pk=None):
        if pk is None:       
            user_obj = User.objects.all()
            user_filter = self.filter_queryset(user_obj)
               
            if user_obj:
                paginator = self.pagination_class
                paginated_queryset = paginator.paginate_queryset(user_filter, request)
                
                user_serializer = GetUsersSeriallizers(paginated_queryset, many=True)
                
                response_data = {
                    'next': paginator.get_next_link(),
                    'previous': paginator.get_previous_link(),
                    'count': paginator.page.paginator.count,    
                    'data': user_serializer.data
                }
                
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
   
    
    # def post(self, request):       
    #     user_serializer = UsersSeriallizers(data=request.data)
        
    #     if user_serializer.is_valid():            
    #         hashed_password = make_password(request.data['password'])
    #         user_serializer.validated_data['password'] = hashed_password
    #         user_serializer.save()
    #         response_data = {
    #             'data' : user_serializer.data
    #         }
    #         return Response(response.successResponse("data view", response_data), status=status.HTTP_201_CREATED)           
    #     else:
    #         return Response(response.errorResponse("HTTP_400_BAD_REQUEST", user_serializer.errors), status=status.HTTP_400_BAD_REQUEST)
    
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
        
class AddressApiView(GenericAPIView):
    
    serializer_class = AddressSerialzers
    
    def get(self, request):
        address_obj = Address.objects.all()
        address_serializer = self.serializer_class(address_obj, many=True)
        if address_obj:
            response_data ={
                "success" : True,
                "data" : address_serializer.data
            }
            return Response(response.successResponse('data view',response_data), status=status.HTTP_200_OK)
        else:
            response_data={
                "success" : False,
                "data" : {
                    "error" : "No data found"
                }
            }
            return Response(response.errorResponse(response_data), status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        address_serialier = self.serializer_class(data=request.data)
        if address_serialier.is_valid():
            address_serialier.save()
            return Response(response.successResponse('data created',address_serialier.data), status=status.HTTP_201_CREATED)
        return Response(response.errorResponse('validation error',address_serialier.errors),status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        address_obj = Address.objects.get(id = pk)
        if address_obj:
            address_obj.delete()
            return Response(response.successResponse('data deleted'),status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(response.errorResponse('No data found'),status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        try:
            address_obj = Address.objects.get(id=pk)
        except:
            return Response(response.errorResponse('No data found'),status=status.HTTP_404_NOT_FOUND)
        adress_serialier = self.serializer_class(address_obj, data=request.data)
        if adress_serialier.is_valid():
            adress_serialier.save()
            return Response(response.successResponse('data updated',adress_serialier.data), status=status.HTTP_201_CREATED)
        else:
            return Response(response.errorResponse('validation error',adress_serialier.errors),status=status.HTTP_400_BAD_REQUEST)
            
class LogoutApiView(GenericAPIView):

    def get(self, request):
        user = request
        logout(user)
        response = CustomResponse()
        return Response(response.successResponse("You have successfully Logged Out"), status=status.HTTP_200_OK)
    


class changepasswordapiview(GenericAPIView):
    global response
    
    def post(self, request):
        serializer = ChangePasswordSerializers(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            password2 = serializer.validated_data['password2']

            if password != password2:
                response_data : {
                    "success" : False,
                    "data" : {
                        "error":"error changing password"
                    }
                }
                return Response(response.errorResponse(response_data), status=status.HTTP_400_BAD_REQUEST)

            user = request.user  
            user.set_password(password)
            user.save()
            
            response_data = {
                "success": True,
                "data": {
                    "message": "Password changed successfully"
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(response.errorResponse('Invalid input'), status=status.HTTP_400_BAD_REQUEST)

        
        
class UserRegistrationAPi(GenericAPIView):
    global response
    permission_classes = [AllowAny]
    def post(self, request):
        reg_serializers = UserRegistrationSerializer(data=request.data)
        if reg_serializers.is_valid():
            # hashed_password = make_password(request.data['password'])
            # reg_serializers.validated_data['password'] = hashed_password
            reg_serializers.save()
            response_data = {
                "success" : True,
                "data" : reg_serializers.data
            }
            return Response(response.successResponse("Data created", response_data), status=status.HTTP_201_CREATED)
        else:
            response_data = {
                "success" : False,
                "data" : {
                    "error" : "error creating data"
                }
            }
            return Response(response.errorResponse(response_data),status=status.HTTP_400_BAD_REQUEST)
    


