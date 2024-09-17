from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import FarmerSerializer
from farmer.models import Farmer
from sendsms.models import Sendsms
from sendsms.utils import send_sms
import random

# Farmer Views

class FarmerListView(APIView):
  
    def get(self, request):
        farmers = Farmer.objects.all()
        farmers_name = request.query_params.get("farmers_name")
        if farmers_name:
            farmers = farmers.filter(farmer_name=farmers_name)
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FarmerDetailView(APIView):

    def get(self, request, id):
        farmer = get_object_or_404(Farmer, id=id)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)

    def put(self, request, id):
        farmer = get_object_or_404(Farmer, id=id)
        serializer = FarmerSerializer(farmer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        farmer = get_object_or_404(Farmer, id=id)
        farmer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# SMS Views

@api_view(['POST'])
def send_sms_view(request):
    phone_number = request.data.get('phone_number')  
    if not phone_number:
        return Response({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        farmer = get_object_or_404(Farmer,phone_number=phone_number)

        message = f"Hello {farmer.farmers_name}, here are your recommendations: [YOUR_RECOMMENDATIONS_HERE]"

        response = send_sms(phone_number, message) 

        if response:
            # Save to database
            Sendsms.objects.create(
                sender_id=random.randint(1000, 9999),  
                recipient=phone_number,
                farmer_id=farmer.farmer_id,
                sensor_id=0,
                message=message
            )
            return Response({"status": "SMS sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to send SMS"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        print(f"An error occurred: {str(e)}")  
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def send_recommendation(request, farmer_id):
   
    try:
        farmer = get_object_or_404(Farmer, id=farmer_id)  
        message = f"Hello {farmer.farmers_name}, here are your recommendations: [YOUR_RECOMMENDATIONS_HERE]"

        response = send_sms(farmer.phone_number, message)  

        if response:
            return Response({'status': 'Recommendation sent successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to send recommendation.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        print(f"An error occurred: {str(e)}")  
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def farmer_detail(request, farmer_id):
  
    try:
        farmer = get_object_or_404(Farmer, id=farmer_id)  
        
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}") 
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
