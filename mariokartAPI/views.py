from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from api.models import Game, Circuit
from api.serializers import GameSerializer, CircuitSerializer


def games_list(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def create_game(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = GameSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def set_game(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = GameSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def games(request):
    if request.method == 'GET':
        return games_list(request)
    elif request.method == 'POST':
        return create_game(request)
    elif request.method == 'PUT':
        return set_game(request)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GameSerializer(game)
        return JsonResponse(serializer.data, status.HTTP_200_OK)

    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)

    return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
def circuit(request, pk):
    try:
        circuit = Circuit.objects.get(pk=pk)
    except Circuit.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return circuit_detail(circuit)
    elif request.method == 'DELETE':
        return delete_circuit(circuit)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def circuit_detail(circuit):
    serializer = CircuitSerializer(circuit)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


def delete_circuit(circuit):
    circuit.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)
