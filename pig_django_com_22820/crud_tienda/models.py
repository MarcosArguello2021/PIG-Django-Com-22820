from tabnanny import verbose
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
    ('VM', 'Vestimenta'),
    ('CA', 'Calzado'),
    ('AC', 'Accesorios'),
    ('SU', 'Suplementos'),
)

SUBCATEGORIA = (
    ('RC', 'Remeras & Chombas'),
    ('BS', 'Bermudas & Shorts'),
    ('BC', 'Buzos & Camperas'),
    ('PC', 'Pantalones & Calzas'),
)

class Item(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Producto')
    precio = models.FloatField()
    foto = models.ImageField(upload_to='productos')
    talle = models.CharField(max_length=2, choices=TALLES, blank=True, null=True)
    info = models.CharField(max_length=250)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    subcategoria = models.CharField(max_length=2, choices=SUBCATEGORIA, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['nombre']  # será ascendente

    def __str__(self):
        return self.nombre
