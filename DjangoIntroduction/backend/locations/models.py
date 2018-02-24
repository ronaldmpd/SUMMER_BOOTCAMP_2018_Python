from django.db import models

# Create your models here.
class Location(models.Model):
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    nombre = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre