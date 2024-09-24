from django.urls import path
from .views import inactive_sensors

urlpatterns = [
    path('',inactive_sensors),
]