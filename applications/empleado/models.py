from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Habilidades(models.Model):
    """Model definition for Habilidad."""
    habilidad= models.CharField('Habilidad', max_length=50)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Habilidad."""
        
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        """Unicode representation of Habilidad."""
        return str(self.id)+' '+self.habilidad


# Create your models here.

class City(models.Model):
    """Model definition for Ciudad."""
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre corto', max_length=15)

    class Meta:
        """Meta definition for Ciudad."""

        verbose_name = 'City'
        verbose_name_plural = 'Citys'

    def __str__(self):
        """Unicode representation of Ciudad."""
        return str(self.id)+' '+self.name


# Create your models here.
class Empleado(models.Model):
    AREA_CHOICES=(
        ('0','OPERATIVA'),
        ('1','ADMINISTRACION'),
        ('2','CONTABILIDAD'),
        ('3','SISTEMAS'),
        ('4','COMPRAS'),
        ('5','VENTAS'),
        ('6','ALAMACEN'),
        ('7','PRODUCCION'),
    )
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    dni = models.CharField('DNI', max_length=8,unique=True)
    edad = models.IntegerField('Edad',blank=True)
    phone = models.CharField('Telefono', max_length=9,unique=True)
    area = models.CharField('Area', max_length=1,choices=AREA_CHOICES,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    habilidad=models.ManyToManyField(Habilidades)
    avatar = models.ImageField( upload_to='empleado',null=True,blank=True)

    class Meta:
        """Meta definition for Empleado."""
        ordering=("id",)
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return (str(self.id)+' '+ 
        self.first_name + ' '+ 
        self.last_name +' '+ 
        str(self.edad) +' '+
        self.phone +' '+
        self.area)
        


# model-vista administrador
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name',
        'edad',
        'phone',
        'dni',
    )
    search_fields=('first_name',)
    filter_horizontal=('habilidad',)