from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from sensorreadings.models import Sensorreadings
from .serializers import SensorreadingsSerializer
from moisturereadings.models import Moisturereadings
from .serializers import MoisturereadingsSerializer


# Create your views here.
class SensorreadingsListView(APIView):
    def get(self, request):
        sensor_readings = Sensorreadings.objects.all()
        sensor_id = request.query_params.get("sensor_id")
        if sensor_id:
            sensor_readings = sensor_readings.filter(sensor_id=sensor_id)
        serializer = SensorreadingsSerializer(sensor_readings, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SensorreadingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SensorreadingsDetailView(APIView):
    def get(self, request, id):
        sensor_reading = get_object_or_404(Sensorreadings, id=id)
        serializer = SensorreadingsSerializer(sensor_reading)
        return Response(serializer.data)
    def put(self, request, id):
        sensor_reading = get_object_or_404(Sensorreadings, id=id)
        serializer = SensorreadingsSerializer(sensor_reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        sensor_reading = get_object_or_404(Sensorreadings, id=id)
        sensor_reading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MoisturereadingsListView(APIView):
    def get(self, request):
        moisture_readings = request.query_params.get("moisture_readings")
        if moisture_readings:
            moisturerecommendations = Moisturereadings.objects.filter(recommendations_content=moisture_readings)
        else:
            moisturerecommendations = Moisturereadings.objects.all()
        serializer = MoisturereadingsSerializer(moisturerecommendations, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MoisturereadingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MoisturereadingsDetailView(APIView):
    def get(self, request, id):
        moisturereading = Moisturereadings.objects.get(id=id)
        serializer = MoisturereadingsSerializer(moisturereading)
        return Response(serializer.data)
    def put(self, request, id):
        moisture_reading = Moisturereadings.objects.get(id=id)
        serializer = MoisturereadingsSerializer(moisture_reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        moisturereading = Moisturereadings.objects.get(id=id)
        moisturereading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)