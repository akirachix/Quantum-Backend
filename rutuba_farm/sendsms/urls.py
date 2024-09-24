
from django.urls import path
from .views import (
    SensorDataCreateView,
    SensorDataListView,
    SensorDataDetailView,
  
)

urlpatterns = [
    path('sensor-data/', SensorDataCreateView.as_view(), name='sensor-data-create'),
    path('sensor-data/list/', SensorDataListView.as_view(), name='sensor-data-list'),
    path('sensor-data/<int:pk>/', SensorDataDetailView.as_view(), name='sensor-data-detail'),
    
   
]

