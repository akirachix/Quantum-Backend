# inactivestatus/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sensor   # Assuming inactive status is tracked by the Sensor model
# from .serializers import SensorSerializer  # Import the correct serializer

# Get Inactive Sensors
@api_view(['GET'])
def get_inactive_sensors(request):
    inactive_sensors = Sensor.objects.filter(is_active=False)
    # serializer = SensorSerializer(inactive_sensors, many=True)
    return Response()
