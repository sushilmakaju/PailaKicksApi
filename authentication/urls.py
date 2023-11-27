from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserAPiView.as_view()),
    path('user/<int:pk>/', UserAPiView.as_view()),
    path('address/', AddressApiView.as_view()),
    path('address/<int:pk>', AddressApiView.as_view()),
    
    path('login/', LoginApi.as_view(), name="login"),
    path('logout/', LogoutApiView.as_view(), name="logout")
]