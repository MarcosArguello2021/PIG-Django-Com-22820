# Generated by Django 3.2 on 2022-10-24 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_tienda', '0003_alter_item_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='foto',
            field=models.ImageField(upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='item',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='talle',
            field=models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2, null=True),
        ),
    ]