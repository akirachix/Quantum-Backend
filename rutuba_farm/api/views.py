from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import FarmerSerializer
from farmer.models import Farmer
from sendsms.models import Sendsms
from sendsms.utils import send_sms
from sensorreadings.models import Sensorreadings
from .serializers import SensorreadingsSerializer
from moisturereadings.models import Moisturereadings
from .serializers import MoisturereadingsSerializer
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from api.serializers import UsersSerializer
from users.models import User
from .serializers import UsersSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recommendations.models import Recommendation
from phreadings.models import PhReading
from inactivestatus.models import Sensor
from .serializers import RecommendationSerializer, PhReadingSerializer, SensorSerializer
import logging

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




logger = logging.getLogger(__name__) 

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
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


class LoginView(APIView):
     def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.info(f'Login attempt for non-existent user: {email}')
            return Response({
                'error': 'User does not exist',
                'signup_required': True
            }, status=status.HTTP_404_NOT_FOUND)
        django_user = authenticate(username=email, password=password)
        if django_user:
            logger.info(f'User logged in successfully: {email}')
            return Response({'Login successful'}, status=status.HTTP_200_OK)
        logger.error(f'Login failed for user: {email}')
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class UsersListView(APIView):
    
    def get(self, request):
        users = User.objects.all() 
        name = request.query_params.get("name")
        if name:
            users = users.filter(firstname=name)  
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
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

class UsersDetailView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UsersSerializer(user, data=request.data)
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
    
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def generate_token(request):
    user, created = User.objects.get_or_create(username=' ')
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    })

class RecommendationDetailedView(APIView):
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








        
   


 
