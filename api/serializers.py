from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Circuit, Game, Character, Cup, Statistic


class CircuitSerializer(serializers.HyperlinkedModelSerializer):
    cups = serializers.HyperlinkedRelatedField(
        view_name='cup-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Circuit
        fields = '__all__'


class GameSerializer(serializers.HyperlinkedModelSerializer):
    cups = serializers.HyperlinkedRelatedField(
        view_name='cup-detail',
        read_only=True,
        many=True,
    )
    characters = serializers.HyperlinkedRelatedField(
        view_name='character-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Game
        fields = '__all__'


class CupSerializer(serializers.HyperlinkedModelSerializer):
    circuits = serializers.HyperlinkedRelatedField(
        view_name='circuit-detail',
        read_only=True,
        many=True,
    )
    game = serializers.HyperlinkedRelatedField(
        view_name='game-detail',
        read_only=True,
    )

    class Meta:
        model = Cup
        fields = '__all__'


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        view_name='game-detail',
        read_only=True,
        many=True,
    )
    statistic = serializers.HyperlinkedRelatedField(
        view_name='statistic-detail',
        read_only=True,
    )

    class Meta:
        model = Character
        fields = '__all__'


class StatisticSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.HyperlinkedRelatedField(
        view_name='character-detail',
        read_only=True,
    )

    class Meta:
        model = Statistic
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
