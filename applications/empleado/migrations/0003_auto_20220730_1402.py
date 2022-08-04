# Generated by Django 3.2.14 on 2022-07-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_empleado_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='dni',
            field=models.CharField(max_length=10, unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='phone',
            field=models.CharField(max_length=10, unique=True, verbose_name='Telefono'),
        ),
    ]