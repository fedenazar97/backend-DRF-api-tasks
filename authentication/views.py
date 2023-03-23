from django.shortcuts import render

from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema


# Create your views here.

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class Login(APIView):
    permission_classes = ()
    
    @extend_schema(
        request=LoginSerializer,
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'token': {'type': 'string'}
                }
            },
            400: {
                'type': 'object',
                'properties': {
                'error': {'type': 'string'}
                }
            }
        },
    )

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'username': user.username, 'token': user.auth_token.key})
        else:
            return Response({'error':'Incorrect credentials'}, status=status.HTTP_400_BAD_REQUEST)
