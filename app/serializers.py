from rest_framework import serializers
from .models import dress_effects, fire_effects


class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = dress_effects
        fields = ['status']


class FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = fire_effects
        fields = ['status']
