
from rest_framework import serializers
from .models import SensorData
from .utils import send_sms
import logging

logger = logging.getLogger(__name__)

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['ph_reading', 'moisture_reading', 'nutrients', 'farmer_id']
       

