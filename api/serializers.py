from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Circuit, Game, Character, Cup, Statistic


class CircuitSerializer(serializers.ModelSerializer):
    cups = serializers.PrimaryKeyRelatedField(many=True, queryset=Cup.objects.all())

    class Meta:
        model = Circuit
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cup
        fields = '__all__'


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedIdentityField(
        view_name='game-detail',
        lookup_field='pk',
        many=True,
    )

    class Meta:
        model = Character
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'