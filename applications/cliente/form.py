from django import forms
from .models import Cliente
from django.core.validators import validate_email,ValidationError

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = ('first_name',
                  'last_name',
                  'email',
                  'telefono',
        )

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Ingrese su Nombre'
        })

        self.fields['last_name'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Ingrese apellidos'
        })

        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Ingrese email. Ejemplo@hotmail.com'
        })
        self.fields['telefono'].widget.attrs.update({
            'class':'form-control'
        })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if validate_email(email):
            print ("es un correo")
        else:
            raise forms.ValidationError("Ingrese un correo valido")
    
        return email

