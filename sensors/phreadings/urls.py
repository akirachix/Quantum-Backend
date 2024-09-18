from django.urls import path
from .views import create_ph_reading

urlpatterns = [
    path('', create_ph_reading),
]
