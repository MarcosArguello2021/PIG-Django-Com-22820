# Generated by Django 3.2 on 2022-12-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_tienda', '0002_rename_item_fk_opciones_vestimenta_vestimenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='calzado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='suplemento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='vestimenta',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
