from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PhReading, Sensor
from .serializers import PhReadingSerializer, SensorSerializer  # Import serializers

@api_view(['GET'])
def get_all_ph_reading(request):
    ph_reading = PhReading.objects.all()
    serializer = PhReadingSerializer(ph_reading, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_inactive_sensors(request):
    inactive_sensors = Sensor.objects.filter(is_active=False)
    serializer = SensorSerializer(inactive_sensors, many=True)
    return Response(serializer.data)
