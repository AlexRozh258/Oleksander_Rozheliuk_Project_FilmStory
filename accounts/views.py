from django.shortcuts import render
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info("User registered: %s", user.username)
            return Response({"detail": "User created"}, status=status.HTTP_201_CREATED)
        logger.info("Registration failed: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    pass


class RefreshView(TokenRefreshView):
    pass


class LogoutView(APIView):
    def post(self, request):
        user = request.user.username if request.user and request.user.is_authenticated else None
        logger.info("Logout requested. user=%s", user)
        return Response({"detail": "Logged out (client should delete tokens)."}, status=status.HTTP_200_OK)
