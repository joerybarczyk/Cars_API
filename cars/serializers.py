from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        '''Define meta-information about CarSerializer'''
        model = Car
        fields = ['id','make','model','year','price']

