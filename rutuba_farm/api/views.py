from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from api.serializers import UsersSerializer
from users.models import User
from .serializers import UsersSerializer
from django.contrib.auth import authenticate
import logging


logger = logging.getLogger(__name__) 

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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









        
   


 