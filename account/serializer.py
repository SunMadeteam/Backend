from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import User, Branch
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get('usertype')!='florist':
            data['branch'] = None
        if datetime.now().day==23:
            salary=10000
        return data
    is_staff = serializers.BooleanField(read_only=True)
    
    class Meta:
        model=User
        fields = ('id', 'name','username','number','is_staff','is_active','is_admin','usertype', 'photo', 'salary', 'branch')

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
