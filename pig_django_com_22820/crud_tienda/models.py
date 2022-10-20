from django.db import models

# Create your models here.
class Calzado(models.Model):
    foto= models.ImageField(upload_to='calzado')
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    info = models.CharField(max_length=200)