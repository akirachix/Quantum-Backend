from django.urls import path
from .views import RecommendationDetailedView, SensorreadingsListView
from .views import SensorreadingsDetailView
from .views import MoisturereadingsListView
from .views import MoisturereadingsDetailView
from django.contrib import admin
from . import views
from api.views import LoginView  
from .views import generate_token 
from .views import UsersListView
from .views import UsersDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import RecommendationListView, InactiveSensorsListView, PhReadingsListView




urlpatterns = [
    path('sensorreadings/',SensorreadingsListView.as_view(),name='sensorreadings_list_view'),
    path('sensorreadings/<int:id>',SensorreadingsDetailView.as_view(),name='sensorreadings_list_view'),
    path('moisturereadings/', MoisturereadingsListView.as_view(),name='moisturereadings_list_view'),
    path('moisturereadings/<int:id>/',MoisturereadingsDetailView.as_view(),name='moisturereadings_detail_view'),
    path('users/<int:id>/', UsersDetailView.as_view(), name='users_detail_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('generate_token/', views.generate_token, name='generate_token'),
    path('users/', views.UsersListView.as_view(), name='users-list'),
    path('register/', views.RegisterView.as_view(), name='register_view'),
    path('recommendation/', RecommendationDetailedView.as_view(), name='recommendation-detail'),
    path('inactive/', InactiveSensorsListView.as_view(), name='inactive_sensors'),
    path('ph-readings/', PhReadingsListView.as_view(), name='list_ph_readings'),

    
]

