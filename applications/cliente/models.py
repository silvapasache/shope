from django.db import models

# Create your models here.

class Cliente(models.Model):
    """Model definition for Cliente."""

    # TODO: Define fields here
    first_name = models.CharField('nombre', max_length=50)
    last_name = models.CharField('apellidos', max_length=50,blank=True)
    email=models.EmailField('Correo',max_length=30,default=" ")
    telefono = models.CharField('telefono', max_length=9)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return self.first_name + self.last_name+ self.telefono

