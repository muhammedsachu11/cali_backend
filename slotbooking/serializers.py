from rest_framework import serializers

from django.contrib.auth.models import User
from .models import AuthUser, Slotdetails, SlotAsscTime

class SlotAsscTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotAsscTime
        fields = '__all__'


class Slotdetailsserializer(serializers.ModelSerializer):  
    class Meta:
        model = Slotdetails
        fields = '__all__'


