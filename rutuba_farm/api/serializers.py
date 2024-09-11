from rest_framework import serializers
from sensorreadings.models import Sensorreadings
from moisturereadings.models import Moisturereadings


class SensorreadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensorreadings
        fields = "__all__"


class MoisturereadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Moisturereadings
        fields="__all__"