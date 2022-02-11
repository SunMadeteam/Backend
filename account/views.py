import datetime
import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from .models import ConfirmCode, User
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

# Create your views here.
from rest_framework.views import APIView


class RegisterAPIView(APIView):
    def post(self,request):
        name=request.data['name']
        number=request.data['number']
        password = request.data['password']
        #photo= request.data['photo']
        user = User.objects.create_user(
            number=number,
            password=password,
            name=name,
            is_active=True,
            #photo=photo,
        )
        code = str(random.randint(1000,9999))
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
        ConfirmCode.objects.create(user=user, code=code, valid_until=valid_until)
        # send_code_to_phone(code,username)
        return Response(data={'message': 'User created!!!'})

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class RegisterStaffAPIView(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self,request):
        name=request.data['name']
        number=request.data['number']
        password = request.data['password']
        usertype= request.data['usertype']
        user = User.objects.create_user(
            number=number,
            password=password,
            name=name,
            is_active=True,
            usertype=usertype
        )
        code = str(random.randint(1000,9999))
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
        ConfirmCode.objects.create(user=user, code=code, valid_until=valid_until)
        # send_code_to_phone(code,username)
        return Response(data={'message': 'Staff created!!!'})
        #return Response(data={'message': f'{request.user.is_staff}'})

class UpdateAPIView(APIView):
    def post(self,request):
        name= request.data['name']
        number = request.data['number']
        password = request.data['password']
        print(number, password)
        user = authenticate(number = number, password=password, name = name)
        print(user)
        if user:
            user.save()
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={
                'token': token.key
            })
        else:
            return Response(data={
                'message': "User not found!"
            }, status = status.HTTP_404_NOT_FOUND)


class LoginAPIView(APIView):
    def post(self, request):
        number = request.data['number']
        password = request.data['password']
        print(number, password)
        user = authenticate(username = number, password=password)
        print(user)
        if user:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={
                'token': token.key
            })
        else:
            return Response(data={
                'message': "User not found!"
            }, status = status.HTTP_404_NOT_FOUND)