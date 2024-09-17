
from rest_framework import serializers
from users.models import User

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


