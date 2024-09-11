from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from recommendations.models import Recommendation
from phreadings.models import PhReading
from inactivestatus.models import Sensor
from .serializers import RecommendationSerializer, PhReadingSerializer, SensorSerializer


class RecommendationListView(APIView):
    def get(self, request, recommendation_id):
        recommendation = get_object_or_404(Recommendation, id=recommendation_id)
        serializer = RecommendationSerializer(recommendation)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InactiveSensorsListView(APIView):
    def get(self, request):
        inactive_sensors = Sensor.objects.filter(is_active=False)
        serializer = SensorSerializer(inactive_sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['is_active'] = False  # Ensure sensor is created as inactive
        serializer = SensorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhReadingsListView(APIView):
    def get(self, request):
        ph_readings = PhReading.objects.all()
        serializer = PhReadingSerializer(ph_readings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
