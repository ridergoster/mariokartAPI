from base64 import b64decode

from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from api.auth import get_or_create_token, get_basic_auth, check_request_token
from api.models import Game, Circuit, Character, Cup
from api.serializers import GameSerializer, CircuitSerializer, CharacterSerializer, CupSerializer, UserSerializer


def create_user(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = UserSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def games_list(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def circuits_list(request):
    circuits = Circuit.objects.all()
    serializer = CircuitSerializer(circuits, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def characters_list(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def cups_list(request):
    cups = Cup.objects.all()
    serializer = CupSerializer(cups, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def game_detail(request, game):
    serializer = GameSerializer(game, context={'request': request})
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


def circuit_detail(request, circuit):
    serializer = CircuitSerializer(circuit, context={'request': request})
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


def character_detail(request, character):
    serializer = CharacterSerializer(character, context={'request': request})
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


def cup_detail(request, cup):
    serializer = CupSerializer(cup, context={'request': request})
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


def create_game(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = GameSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_circuit(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = CircuitSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_character(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = CharacterSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_cup(request):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=400)
    serializer = CupSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_character(request, character):
    try:
        data = JSONParser().parse(request)
    except ParseError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    serializer = CharacterSerializer(character, data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_game(game):
    game.delete()
    return HttpResponse(status=status.HTTP_200_OK)


def delete_circuit(circuit):
    circuit.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


def delete_character(character):
    character.delete()
    return HttpResponse(status=status.HTTP_200_OK)


def delete_cup(cup):
    cup.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def users(request):
    if request.method == 'POST':
        return create_user(request)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def login(request):
    basic = get_basic_auth(request)
    if basic is not None:
        log = b64decode(bytes(basic, 'ascii')).decode('ascii').split(':')
        user = authenticate(username=log[0], password=log[1])
        if user is not None:
            token = get_or_create_token(user)
            return JsonResponse(data={token: token.hash})
    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def games(request):
    if request.method == 'GET':
        return games_list(request)
    elif request.method == 'POST':
        authorized = check_request_token(request)
        if authorized:
            return create_game(request)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def game(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return game_detail(request, game)
    elif request.method == 'DELETE':
        authorized = check_request_token(request)
        if authorized:
            return delete_game(game)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def circuits(request):
    if request.method == 'GET':
        return circuits_list(request)
    elif request.method == 'POST':
        authorized = check_request_token(request)
        if authorized:
            return create_circuit(request)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def circuit(request, pk):
    try:
        circuit = Circuit.objects.get(pk=pk)
    except Circuit.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return circuit_detail(request, circuit)
    elif request.method == 'DELETE':
        authorized = check_request_token(request)
        if authorized:
            return delete_circuit(circuit)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def characters(request):
    if request.method == 'GET':
        return characters_list(request)
    elif request.method == 'POST':
        authorized = check_request_token(request)
        if authorized:
            return create_character(request)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def character(request, pk):
    character = Character.objects.get(pk=pk)
    if request.method == 'GET':
        return character_detail(request, character)
    elif request.method == 'PUT':
        authorized = check_request_token(request)
        if authorized:
            return update_character(request, character)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        authorized = check_request_token(request)
        if authorized:
            return delete_character(character)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def cups(request):
    if request.method == 'GET':
        return cups_list(request)
    elif request.method == 'POST':
        authorized = check_request_token(request)
        if authorized:
            return create_cup(request)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def cup(request, pk):
    try:
        cup = Cup.objects.get(pk=pk)
    except Cup.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return cup_detail(request, cup)
    elif request.method == 'DELETE':
        authorized = check_request_token(request)
        if authorized:
            return delete_cup(cup)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
