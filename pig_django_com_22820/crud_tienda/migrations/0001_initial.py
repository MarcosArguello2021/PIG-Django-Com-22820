# Generated by Django 3.2 on 2022-11-17 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Producto')),
                ('precio', models.FloatField()),
                ('foto', models.ImageField(default='camo-pants.jpg', upload_to='productos')),
                ('info', models.CharField(max_length=250)),
                ('subcategoria', models.CharField(blank=True, choices=[('MO', 'Moda'), ('EN', 'Entrenamiento')], max_length=2, null=True)),
                ('stock', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Calzado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Producto')),
                ('precio', models.FloatField()),
                ('foto', models.ImageField(default='camo-pants.jpg', upload_to='productos')),
                ('info', models.CharField(max_length=250)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Suplemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Producto')),
                ('precio', models.FloatField()),
                ('foto', models.ImageField(default='camo-pants.jpg', upload_to='productos')),
                ('info', models.CharField(max_length=250)),
                ('subcategoria', models.CharField(blank=True, choices=[('PR', 'Proteínas'), ('VT', 'Vitaminas')], max_length=2, null=True)),
                ('stock', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vestimenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Producto')),
                ('precio', models.FloatField()),
                ('foto', models.ImageField(default='camo-pants.jpg', upload_to='productos')),
                ('info', models.CharField(max_length=250)),
                ('subcategoria', models.CharField(blank=True, choices=[('RC', 'Remeras & Chombas'), ('BS', 'Bermudas & Shorts'), ('BC', 'Buzos & Camperas'), ('PC', 'Pantalones & Calzas')], max_length=2, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Opciones_vestimenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2, null=True)),
                ('stock', models.PositiveIntegerField()),
                ('item_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_tienda.vestimenta')),
            ],
        ),
        migrations.CreateModel(
            name='Opciones_calzado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(blank=True, choices=[('34.5', '34.5(3.5 uk)'), ('35.5', '35.5(4 uk)'), ('36', '36(4.5 uk)'), ('38', '38(6 uk)'), ('39', '39(7 uk)'), ('40', '40(8 uk)'), ('41', '41(8.5 uk)'), ('41.5', '41.5(9 uk)'), ('42', '42(9.5 uk)'), ('43', '43(10 uk)'), ('44', '44(11 uk)'), ('45', '45(11.5 uk)')], max_length=4, null=True)),
                ('stock', models.PositiveIntegerField()),
                ('calzado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_tienda.calzado')),
            ],
        ),
    ]
