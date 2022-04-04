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
from .models import User,Branch
from rest_framework.permissions import BasePermission
from .serializer import BranchSerializer, UserSerializer, ChangePassword
from django.shortcuts import get_object_or_404
from shop.models import Delivery
from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import GenericViewSet


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
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
        # send_code_to_phone(code,username)
        return Response(data={'message': 'User created!!!'})
    
    def get(self, request):
        clients=UserSerializer(User.objects.filter(is_staff=False), many=True)
        return Response({"Clients": clients.data, 'user': str(request.user), 'auth': str(request.auth)})


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin

class RegisterStaffAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_staff=True, is_admin=False)
    search_fields = ["number"]
    filterset_fields = [ "is_active", "usertype"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
'''
    def post(self,request):
        name=request.data.get('name')
        number=request.data.get('number')
        password = request.data.get('password')
        usertype = request.data.get('usertype')
        branch=request.data.get('branch')
        user = User.objects.create_user(
            number=number,
            password=password,
            name=name,
            is_staff=True,
            usertype=usertype,
            branch=branch
        )
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
        # send_code_to_phone(code,username)
        return Response(data={'message': 'Staff created!!!'})
    
'''
    
class UpdateStaffAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    '''
    def get(self, request, format=None):
        user = User.objects.filter(is_staff=True, is_admin=False)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''  

class PasswordChange(APIView):
    serializer_class = ChangePassword
    queryset = User.objects.all()
    # permission_classes = (IsSuperuser, )

    def post(self, request):
        number = request.data["number"]
        password = request.data["password"]

        user = User.objects.filter(number=number).first()
        user.set_password(password)
        user.save()
        return Response({"статус": ("Пароль успешно изменён")})
 


class LoginAPIView(APIView):
    def post(self, request):
        number = request.data.get('number')
        password = request.data.get('password')
        #print(number, password)
        user = authenticate(username = number, password=password)
        #print(user)
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

