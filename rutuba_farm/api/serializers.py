from rest_framework import serializers
from .models import Sensor, Recommendation, PhReading

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
