from .views import *
from rest_framework import serializers
from .models import *

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