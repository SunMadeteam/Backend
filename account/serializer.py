from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import User, Branch

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.username = validated_data.get('username', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.usertype = validated_data.get('usertype', instance.usertype)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.branch = validated_data.get('branch', instance.branch)
        instance.save()
        return instance

    class Meta:
        model=User
        fields = ('id', 'name','username','number','is_staff','is_admin','usertype', 'photo', 'salary', 'branch')

class BranchSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Branch.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.adress = validated_data.get('adress', instance.adress)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.schedule = validated_data.get('schedule', instance.schedule)

        instance.save()
        return instance

    class Meta:
        model=Branch
        fields = ('id', 'adress','phone','schedule')
