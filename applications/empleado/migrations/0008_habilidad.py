# Generated by Django 3.2.14 on 2022-08-02 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0007_empleado_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
    ]
