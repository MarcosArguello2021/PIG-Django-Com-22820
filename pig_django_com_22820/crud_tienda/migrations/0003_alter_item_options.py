# Generated by Django 3.2 on 2022-10-23 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_tienda', '0002_auto_20221023_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['nombre'], 'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
    ]
