from rest_framework import serializers
from .models import Sensor, Recommendation, PhReading
from rest_framework import serializers
from recommendations.models import Recommendation
from phreadings.models import PhReading
from inactivestatus.models import Sensor

# Sensor Serializer
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'is_active']  # Add all necessary fields here

# Recommendation Serializer
class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = [
            'id', 'recommendation_content', 'farmer_id', 
            'sensor_id', 'recommendation_id', 'is_active'
        ]  # Add all relevant fields

# PhReadings Serializer
class PhReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhReading
        fields = [
            'id', 'acidic', 'neutral', 'alkaline', 
            'farmer_id', 'ph_id'
        ]  # Add all relevant fields
from sensorreadings.models import Sensorreadings
from moisturereadings.models import Moisturereadings
from users.models import User


class SensorreadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensorreadings
        fields = "__all__"


class MoisturereadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Moisturereadings
        fields="__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)  
        user.save()
        return user

class UsersDetailSerializer(serializers.ModelSerializer):# class RoleSerializer(serializers.Serializer):
#     user_id = serializers.IntegerField()
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'password']
        extra_kwargs = {
            'password': {'read_only': True},
        }



class LoginSerializer(serializers.Serializer):   

    class Meta:
        model = User
        fields = ('username', 'password')



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  
        user.save()
        return user

class UsersDetailSerializer(serializers.ModelSerializer):# class RoleSerializer(serializers.Serializer):
#     user_id = serializers.IntegerField()
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'password']
        extra_kwargs = {
            'password': {'read_only': True},
        }

class LoginSerializer(serializers.Serializer):   
    class Meta:
        model = User
        fields = ('username', 'password')



class MoisturereadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Moisturereadings
        fields="__all__"

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'

class PhReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhReading
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'