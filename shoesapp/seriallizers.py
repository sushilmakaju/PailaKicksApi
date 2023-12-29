from rest_framework import serializers
from .views import *
from .models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class Product_cartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product_cart
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    order_items = Product_cartSerializers(many=True) 
    class Meta:
        model = Order
        fields = '__all__'