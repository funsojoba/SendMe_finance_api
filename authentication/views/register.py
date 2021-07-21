from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers.register_serializer import RegisterSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        data = request.data

        return Response({"data":data})
