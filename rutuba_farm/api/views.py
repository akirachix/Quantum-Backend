from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from phreadings.models import Phreadings
from .serializers import PhreadingsSerializer


# Create your views here.
class PhreadingsListView(APIView):
    def get(self, request):
        farmers_name = request.query_params.get("farmers_name")
        if farmers_name:
            phreadings = Phreadings.objects.filter(farmers_name=farmers_name)
        else:
            phreadings = Phreadings.objects.all()
        serializer = PhreadingsSerializer(phreadings, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PhreadingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PhreadingsDetailView(APIView):
    def get(self, request, id):
        try:
            phreading = Phreadings.objects.get(id=id)
        except Phreadings.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PhreadingsSerializer(phreading)
        return Response(serializer.data)
    def put(self, request, id):
        try:
            phreading = Phreadings.objects.get(id=id)
        except Phreadings.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PhreadingsSerializer(phreading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        try:
            phreading = Phreadings.objects.get(id=id)
        except Phreadings.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        phreading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
