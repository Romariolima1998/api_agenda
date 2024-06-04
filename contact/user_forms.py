from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializers import AuthenticationSerializer

from rest_framework import generics, permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwner


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class LoginView(APIView):
    def get(self, request):
        serializer = AuthenticationSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)

            return Response({"user_id": str(user.id), "Token": str(token), "detail": "Login successful."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
