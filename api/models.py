from django.db import models

# Create your models here.

class Cup(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=500)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='cups')
    retro = models.BooleanField(default=False)

class Circuit(models.Model):
    name = models.CharField(max_length=50)
    cup = models.ManyToManyField(Cup)
    nb_laps = models.IntegerField(default=3)
    img_url = models.CharField(max_length=500)