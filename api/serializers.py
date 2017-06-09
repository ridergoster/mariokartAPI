from rest_framework import serializers
from .models import Circuit, Game, Character, Cup, Statistic

class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = ('name', 'cup', 'nb_laps', 'img_url')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'abbreviation', 'released_date', 'platform', 'cover')

class CupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cup
        fields = ('name', 'img_url', 'game', 'retro')

class CharacterSerializer(serializers.ModelSerializer):#todo
    class Meta:
        model = Character
        fields = ('name', 'img_url', 'game', 'retro')

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('character', 'hours', 'avg_position', 'nb_use')
