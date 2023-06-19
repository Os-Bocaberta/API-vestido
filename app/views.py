from django.http import JsonResponse
from .models import dress_effects, fire_effects
from .serializers import DressSerializer, FireSerializer
from django.shortcuts import render

# Create your views here.


def dress(request):
    statusCode = dress_effects.objects.all().filter(id=1)
    serializedInfo = DressSerializer(statusCode, many=True)

    return JsonResponse(serializedInfo.data, safe=False)


def volcano1(request):
    statusCode = fire_effects.objects.all().filter(id=1)
    serializedInfo = FireSerializer(statusCode, many=True)

    return JsonResponse(serializedInfo.data, safe=False)


def volcano2(request):
    statusCode = fire_effects.objects.all().filter(id=2)
    serializedInfo = FireSerializer(statusCode, many=True)

    return JsonResponse(serializedInfo.data, safe=False)


def volcano3(request):
    statusCode = fire_effects.objects.all().filter(id=3)
    serializedInfo = FireSerializer(statusCode, many=True)

    return JsonResponse(serializedInfo.data, safe=False)
