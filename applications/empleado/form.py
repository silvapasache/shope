from django import forms
from .models import Empleado
from django.core.validators import validate_email
from django.core.validators import ValidationError

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = ('first_name',
                  'last_name',
                  'dni',
                  'edad',
                  'phone',
                  'area',
                  'avatar',  
        )

        widgets={
            'first_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre'
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Apellidos'
                }
            ),
            'dni':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'DNI'
                }
            ),
            'edad':forms.TextInput(
                attrs={
                    'max':'100',
                    'min':'1',
                    'type':'number',
                    'class':'form-control',
                    'placeholder':'0-100'
                }
            ),
            'phone':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su numero'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['area'].widget.attrs.update({
            'class':'form-select'
        })

