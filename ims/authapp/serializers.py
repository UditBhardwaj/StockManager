from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import Usermodel

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Usermodel
        fields = ('id','email','username','password')