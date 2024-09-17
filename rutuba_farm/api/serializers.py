
from rest_framework import serializers
from farmer.models import Farmer
from sendsms.models import Sendsms


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Farmer
        fields="__all__"



class SendsmsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sendsms
        fields="__all__"



