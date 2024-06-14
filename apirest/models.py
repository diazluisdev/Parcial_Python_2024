from django.db import models

class Persona (models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    identificacion = models.CharField(max_length=15)
    edad = models.PositiveSmallIntegerField()
    pais = models.CharField(max_length=50)