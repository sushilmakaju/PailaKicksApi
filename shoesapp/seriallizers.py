from rest_framework import serializers
from .views import *
from .models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = '__all__'
        
class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        models = Brand
        fields = '__all__'

class Product_BrandSerializers(serializers.ModelSerializer):
    class Meta:
        models = Product_Brand
        fields = '__all__'
    
class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        models = ProductImage
        fields = '__all__'