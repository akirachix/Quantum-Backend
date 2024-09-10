

from rest_framework import serializers
from phreadings.models import Phreadings
class PhreadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phreadings
        fields = '__all__'