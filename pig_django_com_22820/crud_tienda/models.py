from random import choices
from statistics import mode
from django.db import models

# Create your models here.
class Item(models.Model):
    TALLES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    SEXO = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
    )
    talle = models.CharField(max_length=2, choices=TALLES)
    foto= models.ImageField(upload_to='calzado')
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    info = models.CharField(max_length=200)
    stock = models.IntegerField()
    tipo = models.CharField()
    sexo = models.CharField(max_length=1,choices=SEXO)
