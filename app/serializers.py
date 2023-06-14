from rest_framework import serializers
from .models import status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = ['status']
