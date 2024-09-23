# # sendsms/urls.py

# from django.urls import path
# from .views import send_sms_view
# from .views import SensorDataCreateView
# from .views import SendSensorDataView
# from .views import ( SendSensorDataView,SensorDataListView,SensorDataDetailView
#                     # ,FarmListView,FarmDetailView
# )


# urlpatterns = [
#     path('send-sms/', send_sms_view, name='send_sms_view'),
#     path('sensor-data/', SensorDataCreateView.as_view(), name='create-sensor-data'),
#     path('send-sensor-data/', SendSensorDataView.as_view(), name='send_sensor_data'),
#     path('sensor-data/', SensorDataListView.as_view(), name='sensor_data_list'),
#     path('sensor-data/<int:id>/', SensorDataDetailView.as_view(), name='sensor_data_detail'),
#     # path('farms/', FarmListView.as_view(), name='farm_list'),
#     # path('farms/<int:id>/', FarmDetailView.as_view(), name='farm_detail'),
#     path('sensorreadings/', SensorDataListView.as_view(), name='sensorreadings_list_view'),
 
# ]
# sendsms/urls.py

from django.urls import path
from .views import SensorDataCreateView
from .views import SendSensorDataView
from .views import SensorDataListView
from .views import SensorDataDetailView
# Remove the import of send_sms_view since it's no longer in your views

urlpatterns = [
    # Removed send_sms_view path since it is not needed anymore
    path('sensor-data/', SensorDataCreateView.as_view(), name='create-sensor-data'),
    path('send-sensor-data/', SendSensorDataView.as_view(), name='send_sensor_data'),
    path('sensor-data-list/', SensorDataListView.as_view(), name='sensor_data_list'),  # Changed to avoid conflict
    path('sensor-data/<int:id>/', SensorDataDetailView.as_view(), name='sensor_data_detail'),
    path('sensorreadings/', SensorDataListView.as_view(), name='sensorreadings_list_view'),
]
