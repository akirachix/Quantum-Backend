
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






































# from django.urls import path
# from .views import SensorDataCreateView
# from .views import SendSensorDataView
# from .views import SensorDataListView
# from .views import SensorDataDetailView

# urlpatterns = [
#     path('sensor-data/', SensorDataCreateView.as_view(), name='create-sensor-data'),
#     path('send-sensor-data/', SendSensorDataView.as_view(), name='send_sensor_data'),
#     path('sensor-data-list/', SensorDataListView.as_view(), name='sensor_data_list'),  # Changed to avoid conflict
#     path('sensor-data/<int:id>/', SensorDataDetailView.as_view(), name='sensor_data_detail'),
#     path('sensorreadings/', SensorDataListView.as_view(), name='sensorreadings_list_view'),
# ]
