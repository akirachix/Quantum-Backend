
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from farmer.models import Farmer
from rest_framework.views import APIView
from .models import SensorData
from .serializers import SensorDataSerializer
from django.views import View
from django.http import JsonResponse
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

class SensorDataCreateView(APIView):
    def post(self, request, format=None):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Just save, don't send SMS here
            return Response({"status": "Sensor data created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendSensorDataView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SensorDataSerializer(data=request.data)

        if serializer.is_valid():
            sensor_data = SensorData.objects.create(
                farmer_id=serializer.validated_data['farmer_id'],
                ph_reading=serializer.validated_data['ph_reading'],
                moisture_reading=serializer.validated_data['moisture_reading'],
                nutrients=serializer.validated_data['nutrients']
            )
            return Response({
                "status": "Sensor data created successfully",
                "created_at": sensor_data.created_at,
                "updated_at": sensor_data.updated_at
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorDataListView(View):
    def get(self, request):
        sensor_data = SensorData.objects.all()
        data = [{"ph_reading": sd.ph_reading, "moisture_reading": sd.moisture_reading} for sd in sensor_data]
        return JsonResponse(data, safe=False)

    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            sensor_data = serializer.save()  
            return JsonResponse({"status": "Sensor data created successfully"}, status=status.HTTP_201_CREATED)
        
        logger.error(f"Validation errors: {serializer.errors}")
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorDataDetailView(View):
    def get(self, request, pk):
        try:
            sensor_data = SensorData.objects.get(pk=pk)
            return JsonResponse({
                'ph_reading': sensor_data.ph_reading,
                'moisture_reading': sensor_data.moisture_reading,
                'nutrients': sensor_data.nutrients
            })
        except SensorData.DoesNotExist:
            return JsonResponse({'error': 'Sensor data not found'}, status=404)

@csrf_exempt
class SensorreadingsListView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
