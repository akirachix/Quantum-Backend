from django.contrib import admin
from django.urls import path

from . import views
from django.urls import path
from api.views import LoginView  
from .views import generate_token 
from .views import UsersListView
from .views import UsersDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [

    path('users/<int:id>/', UsersDetailView.as_view(), name='users_detail_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('generate_token/', views.generate_token, name='generate_token'),
    path('users/', views.UsersListView.as_view(), name='users-list'),
    path('register/', views.RegisterView.as_view(), name='register_view'),
    
]