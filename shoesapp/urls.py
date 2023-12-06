from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductAiView.as_view(), name='product'),
    path('product/<int:pk>/', ProductAiView.as_view(), name='product'),
    
]
