from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from npkreading.models import NpkReading
from .serializers import NpkReadingSerializer
from recommendations.models import Recommendations
from .serializers import RecommendationsSerializer

class NpkReadingListView(APIView):
    def get(self, request):
        npkreading = NpkReading.objects.all()
        
        npk_value = request.query_params.get("npkreading")
        if npk_value:
            npkreading = npkreading.filter(npk_reading=npk_value)  
        
        serializer = NpkReadingSerializer(npkreading, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NpkReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NpkReadingDetailView(APIView):
    def get(self, request, id):
        npkreading = get_object_or_404(NpkReading, id=id)
        serializer = NpkReadingSerializer(npkreading)
        return Response(serializer.data)
    
    def put(self, request, id):
        npkreading = get_object_or_404(NpkReading, id=id)
        serializer = NpkReadingSerializer(npkreading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        npkreading = get_object_or_404(NpkReading, id=id)
        npkreading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecommendationsListView(APIView):
    def get(self, request):
        recommendations = Recommendations.objects.all()
        serializer = RecommendationsSerializer(recommendations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecommendationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecommendationsDetailView(APIView):
    def get(self, request, id):
        recommendation = get_object_or_404(Recommendations, id=id)
        serializer = RecommendationsSerializer(recommendation)
        return Response(serializer.data)
    
    def put(self, request, id):
        recommendation = get_object_or_404(Recommendations, id=id)
        serializer = RecommendationsSerializer(recommendation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        recommendation = get_object_or_404(Recommendations, id=id)
        recommendation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
