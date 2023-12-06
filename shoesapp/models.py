from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_image = models.ImageField()
    product_size = models.IntegerField()
    product_quantity = models.IntegerField()
    description = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=200)
    product_price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

