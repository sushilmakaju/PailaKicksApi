from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
class Product_Brand(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_qty = models.IntegerField()
    
class ProductImage(models.Model):
    Image = models.ImageField()
    product_brand_id = models.ForeignKey(Product_Brand,on_delete=models.CASCADE)