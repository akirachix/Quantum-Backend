from rest_framework import serializers
from npkreading.models import NpkReading
from recommendations.models import Recommendations



class NpkReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model=NpkReading
        fields="__all__"




class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = "__all__"

