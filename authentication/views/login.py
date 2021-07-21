from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from authentication.models.user import User
from authentication.serializers.login_serializer import LoginSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')

        if not email or not password:
            return Response({"error": "both email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if not user:
            raise ValidationError("User does not exist")

        if not user.check_password(password):
            raise ValidationError("password is incorrect")

        serializer = self.serializer_class(user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "success"}, status=status.HTTP_200_OK)
