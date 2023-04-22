from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','username','password',)

        def create(self, validated_data):
            user = CustomUser.objects.create_user(validated_data['username'],password = validated_data['password'],
            email = validated_data['email'])
            return user

