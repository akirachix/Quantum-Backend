from django.urls import path
from . import views

urlpatterns = [
    path('api/inactive/', views.get_inactive_sensors, name='get_inactive_sensors'),
    path('api/recommendation/<int:recommendation_id>/', views.get_recommendation_by_id, name='get_recommendation_by_id'),
    path('api/ph-reading/', views.get_all_ph_readings, name='get_all_ph_reading'),
]
