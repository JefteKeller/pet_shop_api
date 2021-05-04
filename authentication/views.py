from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer, CredentialSerializer


class UserView(APIView):
    def get(self, request):
        user_list = User.objects.all()
        user_serializer = UserSerializer(user_list, many=True)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if not user_serializer.is_valid():
            return Response(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        new_user = User.objects.create_user(  # type:ignore
            username=request.data['username'],
            password=request.data['password'],
        )
        new_user_serializer = UserSerializer(new_user)

        return Response(new_user_serializer.data,
                        status=status.HTTP_201_CREATED)


class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                'user': request.user.username,
                'authenticated': True
            },
            status=status.HTTP_200_OK,
        )


class LoginView(APIView):
    def post(self, request):
        cred_serializer = CredentialSerializer(data=request.data)

        if not cred_serializer.is_valid():
            return Response(cred_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=request.data['username'],
            password=request.data['password'],
        )
        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response(
                {'access_token': token.key},
                status=status.HTTP_200_OK,
            )

        return Response(
            {'message': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED,
        )
