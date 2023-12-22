from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserAPiView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserAPiView.as_view(), name='user_detail'),
    
    path('address/', AddressApiView.as_view()),
    path('address/<int:pk>/', AddressApiView.as_view()),
    
    path('login/', LoginApi.as_view(), name="login"),
    path('logout/', LogoutApiView.as_view(), name="logout"),
    
    path('changepassword/', changepasswordapiview.as_view(), name="changepassword"),
    
    path('registration/', UserRegistrationAPi.as_view(), name='registration')
]