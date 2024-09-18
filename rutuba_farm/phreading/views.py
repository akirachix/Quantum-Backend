# phreading/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PhReading # Ensure you're importing the correct model
from .serializers import PhReadingSerializer  # Ensure you're importing the correct serializer

# Get All PhReadings
@api_view(['GET', 'POST'])
def get_all_ph_readings(request):
    if request.method == 'GET':
        ph_readings = PhReading.objects.all()  # Check if the model is correctly spelled
        serializer = PhReadingSerializer(ph_readings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PhReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
