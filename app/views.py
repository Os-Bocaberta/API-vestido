from django.http import JsonResponse
from .models import dress_effects, fire_effects
from .serializers import DressSerializer, FireSerializer
from django.shortcuts import render

# Create your views here.


def dress(request):
    statusCode = dress_effects.objects.all().filter(id=1)
    serializedInfo = DressSerializer(statusCode, many=True)

    return JsonResponse(serializedInfo.data, safe=False)


def fireEffects(request):
    statusCode = fire_effects.objects.all().filter(id__range=(1, 6))
    serializedInfo = FireSerializer(statusCode, many=True)

    return JsonResponse(serializedInfo.data, safe=False)


def fireEffectsController(request):
    statusCode = fire_effects.objects.all().filter(
        id__range=(1, 6)).values_list('id', 'status', 'name')

    if request.method == 'POST':
        for x in range(1, 7):
            data = request.POST.get(str(x))
            if (data == 'on'):
                dataSave = fire_effects(
                    id=x, name=statusCode[x - 1][2], status=1)
                dataSave.save()
            else:
                dataSave = fire_effects(
                    id=x, name=statusCode[x - 1][2], status=0)
                dataSave.save()

    return render(request, 'fireEffectsController.html', {'status': statusCode})


def dressEffectsController(request):
    statusCode = dress_effects.objects.all().filter(id=1).values('status')

    if request.method == 'POST':
        for x in range(1, 6):
            data = request.POST.get(str(x))
            if (data == 'on'):
                dataSave = dress_effects(
                    id=1, status=x - 1)
                dataSave.save()

    return render(request, 'dressEffectsController.html', {'status': statusCode})
