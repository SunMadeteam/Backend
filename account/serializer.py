from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import User, Branch
from datetime import datetime
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField

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
        fields='__all__'

class UserBranch(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    branch=PresentablePrimaryKeyRelatedField(queryset=Branch.objects.all(), presentation_serializer=BranchSerializer)
    
    def validate(self, data):
        if data.get('usertype')!="florist":
            data['branch'] = None
        print(datetime.now().day)
        if datetime.now().day==24:
            data['salary']=10000
        return data
    is_staff = serializers.BooleanField(read_only=True)
    
    class Meta:
        model=User
        fields = ('id', 'name','username','number','is_staff','is_active','is_admin','usertype', 'photo', 'salary', 'branch')

