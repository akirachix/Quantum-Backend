
from venv import logger
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer
from django.views import View
from django.http import JsonResponse
from sendsms.models import SensorData

class SensorDataCreateView(APIView):
    def post(self, request, format=None):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({"status": "Sensor data created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorDataListView(APIView):
    def get(self, request):
        sensor_data = SensorData.objects.all()
        data = [{"ph_reading": sd.ph_reading, "moisture_reading": sd.moisture_reading ,sd.nutrients:"nutrients"} for sd in sensor_data]
        return Response(data)
  

    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            sensor_data = serializer.save()  
            return Response({"status": "Sensor data created successfully"}, status=status.HTTP_201_CREATED)
        
        logger.error(f"Validation errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SensorDataDetailView(View):
    def get(self, request, pk):
        try:
            sensor_data = SensorData.objects.get(pk=pk)
            return JsonResponse({
                'ph_reading': sensor_data.ph_reading,
                'moisture_reading': sensor_data.moisture_reading,
                'nutrients': sensor_data.nutrients,
                'created_at': sensor_data.created_at,
                'updated_at': sensor_data.updated_at,
            })
        except SensorData.DoesNotExist:
            return JsonResponse({'error': 'Sensor data not found'}, status=404)


