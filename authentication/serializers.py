from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from user.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True, style={'input_type': 'password'})

    class Meta:
        fields = ['username', 'password']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """User Registration Serializer."""

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = self.Meta.model.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }
