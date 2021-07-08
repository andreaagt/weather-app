from django.db import models

# Create your models here.

class Consultas(models.Model):
  location = models.CharField(max_length=2000)
  clima = models.CharField(max_length=2000)
  humedad = models.CharField(max_length=2000)
  temp_min = models.CharField(max_length=2000)
  temp_max = models.CharField(max_length=2000)

  def __str__(self):
    return self.location
