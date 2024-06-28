from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Account


class AccountModelDataGetSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email']


class AccountModelRegisterSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'role']


class AccountModelLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
