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

    # confirm_password = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
        # reg_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        user = self.Meta.model.objects.create(**validated_data)
        return user

    # def validate(self, data):
    #     password = data.get('password')
    #     confirm_password = data.get('confirm_password')
    #
    #     if not data.get('password') or not data.get('confirm_password'):
    #         raise serializers.ValidationError("Please enter a password and "
    #             "confirm it.")
    #
    #     if password != confirm_password:
    #         raise serializers.ValidationError({"pass_not_match": "Those passwords don't match."})
    #
    #     return data

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            },
            # 'confirm_password': {'write_only': True},

        }
