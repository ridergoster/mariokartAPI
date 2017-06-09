import datetime

from django.db import models
from django.utils import timezone


def get_expiration_date():
    return timezone.now() + datetime.timedelta(days=1)


class Token(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, unique=True)
    hash = models.CharField(max_length=100)
    expiration_date = models.DateTimeField(default=get_expiration_date)

    def is_expired(self):
        return self.expiration_date < timezone.now()


class Game(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    released_date = models.DateField(
        blank=True,
        null=True,
    )
    platform = models.CharField(max_length=15)
    cover = models.URLField(blank=True)

    def __str__(self):
        return "%s" % self.name


class Cup(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=500, blank=True)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='cups',
    )
    retro = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.name


class Circuit(models.Model):
    name = models.CharField(max_length=50)
    cups = models.ManyToManyField(
        Cup,
        related_name='circuits',
    )
    nb_laps = models.IntegerField(default=3)
    img_url = models.CharField(
        max_length=500,
        blank=True,
    )

    def __str__(self):
        return "%s" % self.name


class Character(models.Model):
    name = models.CharField(max_length=30)
    birthDate = models.DateTimeField(
        blank=True,
        null=True,
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknow'),
    )
    WEIGHT = (
        ('L', 'Light'),
        ('M', 'Medium'),
        ('H', 'Heavy'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default='U',
    )
    weight = models.CharField(
        max_length=1,
        choices=WEIGHT,
        default='M',
    )
    games = models.ManyToManyField(
        Game,
        related_name="characters",
        blank=True,
    )

    def __str__(self):
        return "%s" % self.name


class Statistic(models.Model):
    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    hours = models.IntegerField(
        default=0,
    )
    avg_position = models.IntegerField(
        default=8,
    )
    nb_use = models.IntegerField(
        default=0,
    )
