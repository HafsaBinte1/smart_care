# serializers python k json a convert kore
from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Service
        fields = '__all__' 