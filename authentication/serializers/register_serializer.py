from rest_framework import serializers
from authentication.models.user import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'