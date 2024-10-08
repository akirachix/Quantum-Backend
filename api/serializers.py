from rest_framework import serializers
from sensorreadings.models import Sensorreadings
from moisturereadings.models import Moisturereadings
from users.models import User
from recommendation.models import Recommendation
from phreadings.models import PhReading
from inactivestatus.models import Sensor
from farmer.models import Farmer
from npkreadings.models import NpkReading


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Farmer
        fields="__all__"


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
    

class UsersDetailSerializer(serializers.ModelSerializer):
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



    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  
        user.save()
        return user


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

        
class NpkReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model=NpkReading
        fields="__all__"


