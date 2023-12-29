from django.db import models
from authentication.models import *

# Create your models here.

order_status = [('Pending' , 'Pending'), ('Shipping', 'Shipping')]

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_image = models.ImageField(null=True, blank=True)
    product_size = models.CharField(max_length=200)
    product_quantity = models.IntegerField()
    description = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=200)
    product_price = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    orderstats = models.BooleanField(default=False)
    
        
    

class Product_cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    orderstats = models.BooleanField(default=False)
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=50, choices=order_status, default='Pending')
    order_items = models.ManyToManyField(Product_cart)
    total = models.FloatField(default=0.0)

    # def save(self, *args, **kwargs):
    #     # Calculate the total before saving the order
    #     self.total = sum(item.price for item in self.order_items.all())
    #     super().save(*args, **kwargs)