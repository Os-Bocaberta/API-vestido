from django.http import JsonResponse
from .models import status
from .serializers import StatusSerializer
from django.shortcuts import render

# Create your views here.


def index(request):
    statusCode = status.objects.all()
    serializedInfo = StatusSerializer(statusCode, many=True)

    return JsonResponse(serializedInfo.data, safe=False)
