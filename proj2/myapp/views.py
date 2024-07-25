from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .serializer import UserSerializer, NewUserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import NewUserModel
from django.core.exceptions import ObjectDoesNotExist

# user register view
class register_user(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# new user register view
class new_user_register(APIView):
    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class new_user_login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = NewUserModel.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
