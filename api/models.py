from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    released_date = models.DateField
    platform = models.CharField(max_length=15)
    cover = models.URLField

    def __str__(self):
        return "%s" % self.name
