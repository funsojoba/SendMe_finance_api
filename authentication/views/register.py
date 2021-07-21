from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers.register_serializer import RegisterSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            first_name = serializer.data.get('first_name', '')
            last_name = serializer.data.get('last_name', '')
            email = serializer.data.get('email', '')
            password = serializer.data.get('password', '')
            
            user = get_user_model().objects.create(email=email, password=password, first_name=first_name,
                                                   last_name=last_name)
            user.set_password(password)
            user.save()
            return Response({"data":serializer.data, "message":"success"}, status=status.HTTP_201_CREATED)

        return Response({"data":serializer.errors, "message":"failure"}, status=status.HTTP_400_BAD_REQUEST)
