from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserAPi.as_view()),
    path('user/<int:pk>', UserAPi.as_view()),
    
    path('login/', LoginApi.as_view(), name="login"),
]