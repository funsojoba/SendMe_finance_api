from rest_framework import serializers
from django.contrib.auth import get_user_model


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, style={
                                     "input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']
