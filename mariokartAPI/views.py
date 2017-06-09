from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from api.models import Circuit
from api.serializers import CircuitSerializer


def circuits_list(request):
    circuits = Circuit.objects.all()
    serializer = CircuitSerializer(circuits, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def create_circuit(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = CircuitSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def circuits(request):
    if request.method == 'GET':
        return circuits_list(request)
    elif request.method == 'POST':
        return create_circuit(request)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def circuit_detail(request, pk):
    try:
        circuit = Circuit.objects.get(pk=pk)
    except Circuit.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CircuitSerializer(circuit)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        circuit.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)