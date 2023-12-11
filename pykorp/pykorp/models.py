from django.db import models
from django.contrib.auth.models import User

class Colis(models.Model):
    numero = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Evenement(models.Model):
    colis = models.ForeignKey(Colis, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()