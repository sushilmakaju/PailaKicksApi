
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UsersSeriallizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class GetUsersSeriallizers(serializers.ModelSerializer):     
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'password',  'user_type']

class AddressSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
    

class ChangePasswordSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60,write_only=True)
    password2 = serializers.CharField(max_length=60, write_only=True)

    class Meta:
        model = User  
        fields = ['password', 'password2']
        



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password',]  
        
    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
