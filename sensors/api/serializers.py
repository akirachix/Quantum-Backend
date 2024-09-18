from rest_framework import serializers
from recommendations.models import Recommendation
from phreadings.models import PhReading
from inactivestatus.models import Sensor

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
