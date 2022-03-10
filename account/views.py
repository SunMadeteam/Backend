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
from .models import ConfirmCode, User,Branch
from rest_framework.permissions import BasePermission
from .serializer import BranchSerializer, UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import generics


class RegisterAPIView(APIView):
    def post(self,request):
        name=request.data.get('name')
        number=request.data.get('number')
        password = request.data.get('password')
        #photo= request.data['photo']
        user = User.objects.create_user(
            number=number,
            password=password,
            name=name,
            is_staff=False
            #photo=photo,
        )
        code = str(random.randint(1000,9999))
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
        ConfirmCode.objects.create(user=user, code=code, valid_until=valid_until)
        # send_code_to_phone(code,username)
        return Response(data={'message': 'User created!!!'})
    
    def get(self, request):
        clients=UserSerializer(User.objects.all().filter(is_staff=False), many=True)
        return Response({"Clients": clients.data, 'user': str(request.user), 'auth': str(request.auth)})


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin

class RegisterStaffAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        user = get_object_or_404(User.objects.filter(is_staff=True), pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self,request):
    #     name=request.data.get('name')
    #     number=request.data.get('number')
    #     password = request.data.get('password')
    #     usertype= request.data.get('usertype')
    #     branch = request.data.get('branch')
    #     # if usertype!=2:
    #     #     branch=null
    #     user = User.objects.create_user(
    #         number=number,
    #         password=password,
    #         name=name,
    #         is_active=True,
    #         usertype=usertype,
    #         is_staff=True,
    #         # branch=branch,
    #     )
    #     code = str(random.randint(1000,9999))
    #     valid_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
    #     ConfirmCode.objects.create(user=user, code=code, valid_until=valid_until)
    #     # send_code_to_phone(code,username)
    #     return Response(data={'message': f'Staff {user.id} created!!!'})
    # def get(self, request):
    #     staff=UserSerializer(User.objects.all().filter(is_staff=True), many=True)
    #     return Response({"Staff": staff.data, 'user': str(request.user), 'auth': str(request.auth)})


class LoginAPIView(APIView):
    def post(self, request):
        number = request.data.get('number')
        password = request.data.get('password')
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
            }, status = status.HTTP_400_BAD_REQUEST)

# class BranchAPIView(APIView):
#     def get(self, request):
#         serializer=BranchSerializer(Branch.objects.all(), many=True)
#         return Response(serializer.data)
#     '''def get(self, request):
#         serializer = BranchSerializer(Branch.objects.all(), many=True)
#         return Response({"branch": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})'''
#     def post(self, request):
#         branch = request.data.get('branch')
#         serializer = BranchSerializer(data=branch)
#         if serializer.is_valid(raise_exception=True):
#             branch_saved = serializer.save()
#         return Response({"success": "Branch {} {} created".format(branch_saved.adress,branch_saved.id)})

class BranchAPIView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

