from django.db import models

# Create your models here.

# Choices
CATEGORIAS = (
    ('VM', 'Vestimenta'),
    ('CA', 'Calzado'),
    ('AC', 'Accesorios'),
    ('SU', 'Suplementos'),
)

SEXO = (
    ('M', 'Mujer'),
    ('H', 'Hombre'),
)

class Item(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Producto')
    precio = models.FloatField()
    foto = models.ImageField(upload_to='productos')
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    # talle = models.CharField(max_length=2,choices=TALLESVES,blank=True, null=True) #elif categoria == 'CA': if sexo == 'M': choices == TALLESZAPMU elif sexo == 'H': choices == TALLESZAPHO), blank=True, null=True)
    info = models.CharField(max_length=250)
    stock = models.IntegerField()
    # subcategoria = models.CharField(max_length=2, choices=SUBCATEGORIA, blank=True, null=True)
    # sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

class Vestimenta(Item):

    SUBCATEGORIA = (
    ('RC', 'Remeras & Chombas'),
    ('BS', 'Bermudas & Shorts'),
    ('BC', 'Buzos & Camperas'),
    ('PC', 'Pantalones & Calzas'),
    )

    TALLES = (
    ('XS', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    )
    
    talle = models.CharField(max_length=2,choices=TALLES,blank=True, null=True)

    subcategoria = models.CharField(max_length=2, choices=SUBCATEGORIA, blank=True, null=True)

    sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=True)

class Calzado(Item):

    TALLES = (
    ('34.5', '34.5(3.5 uk)'),
    ('35.5', '35.5(4 uk)'),
    ('36', '36(4.5 uk)'),
    ('38', '38(6 uk)'),
    ('39', '39(7 uk)'),
    ('40', '40(8 uk)'),
    ('41', '41(8.5 uk)'),
    ('41.5', '41.5(9 uk)'),
    ('42', '42(9.5 uk)'),
    ('43', '43(10 uk)'),
    ('44', '44(11 uk)'),
    ('45', '45(11.5 uk)'),
)
    
    talle = models.CharField(max_length=4,choices=TALLES,blank=True, null=True)

    sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=True)

class Suplemento(Item):

    SUBCATEGORIA = (
        ('PR', 'Proteínas'),
        ('VT', 'Vitaminas'),
    )
    
    subcategoria = models.CharField(max_length=2, choices=SUBCATEGORIA, blank=True, null=True)

class Accesorio(Item):

    SUBCATEGORIA = (
    ('MO', 'Moda'),
    ('EN', 'Entrenamiento'),
    )

    subcategoria = models.CharField(max_length=2, choices=SUBCATEGORIA, blank=True, null=True)
