from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductAiView.as_view(), name='product'),
    path('product/<int:pk>/', ProductAiView.as_view(), name='product'),
    
    path('cart/', CartApiView.as_view(), name='cart'),
    path('cart/<int:pk>/', CartApiView.as_view(), name='cart'),
    
    path('product-cart/', Product_cartApiView.as_view(), name="productcart"), 
    path('product-cart/<int:pk>/', Product_cartApiView.as_view(), name="productcart"), 
    
    path('order/', OrderApiView.as_view(), name="order-api-view")
    
]
