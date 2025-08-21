from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny ,IsAuthenticated
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer

# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self ,request):
        username = request.data.get('username')
        email = request.data.get('email')
        # phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not username or not email  or not password :
            return Response({'error':"All fields are required!"},status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error':"Username already exists!"},status=status.HTTP_400_BAD_REQUEST)
        


        user = User.objects.create(
            username = username ,
            email = email ,
            # phone_number = phone_number ,
            password = make_password(password),
        )

        serializer = UserSerializer(user)
        refresh = RefreshToken.for_user(user)

        return Response({
            'message':'User created successfuly',
            'user': serializer.data ,
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
        },status= status.HTTP_201_CREATED)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try :
            refresh_token = request.data.get("refresh")

            if not refresh_token :
                return Response({'error':'Refresh token is required'},status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message':'Successfuly logout'},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error':'Invalid token'},status=status.HTTP_400_BAD_REQUEST)
        