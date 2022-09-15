from .models import * 
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class ICategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ICategory
        fields = "__all__"
        
class IProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IProgram
        fields = "__all__"
        
