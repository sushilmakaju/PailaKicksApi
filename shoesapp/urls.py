from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductAiView.as_view(), name='product'),
    path('product/<int:pk>/', ProductAiView.as_view(), name='product'),
    
    path('brand/', BrandApiView.as_view(), name='brand'),
    path('brand/<int:pk>/', BrandApiView.as_view(), name='brand'),
    
    path('product-brand/', ProductBrandApiview.as_view(), name='product-brand'),
    path('product-brand/<int:pk>/', ProductBrandApiview.as_view(), name='product-brand'),
    
    path('product-image/', ProductImageApiview.as_view(), name='productimage'),
]
