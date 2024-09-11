from django.urls import path
from .views import get_inactive_sensors

urlpatterns = [
    path('', get_inactive_sensors),
]
