from random import choices
from statistics import mode
from django.db import models

# Create your models here.

# Choices
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
CATEGORIAS = (
    ('RC','Remeras & Chombas'),
    ('BS','Bermudas & Shorts'),
    ('BC','Buzos & Camperas'),
    ('PC','Pantalones & Calzas'),
    ('CA','Calzado'),
    ('AC','Accesorios'),
    ('SU','Suplementos'),
)


class Item(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    foto= models.ImageField(upload_to='calzado')
    talle = models.CharField(max_length=2, choices=TALLES)
    info = models.CharField(max_length=250)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=2,choices=CATEGORIAS)
    sexo = models.CharField(max_length=1,choices=SEXO)
