from django.db import models
from  django.contrib.auth.models import AbstractUser


usertype_list = [('Buyer', 'Buyer'), ('Seller', 'Seller')]
# Create your models here.


class Address(models.Model):
    province = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.IntegerField()

class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default='User')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    user_type = models.CharField(max_length=50, choices=usertype_list)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']