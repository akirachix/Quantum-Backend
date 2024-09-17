# sendsms/serializers.py

from rest_framework import serializers
from .models import Sendsms

class SendsmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sendsms
        fields = ['sender_id', 'recipient', 'farmer_id', 'sensor_id', 'message']
