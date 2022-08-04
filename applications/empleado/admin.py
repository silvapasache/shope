from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Habilidades)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(City)