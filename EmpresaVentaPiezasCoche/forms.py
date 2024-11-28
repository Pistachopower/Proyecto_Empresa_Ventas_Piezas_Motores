#debes colocar esto para trabajar con tus formularios
from django import forms

#importamos el modelo para usarlo en el formulario
from .models import Proveedor

"""
usamos forms.ModelForm para crear un formulario basado en un modelo especifco
"""

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor #llamamos al modelo a utilizar
        #indicamos los campos del modelo
        fields=  ['proveedor', 'telefono', 'correo', 'direccion']
        
        #Personalizamos los campos con clases CSS y placeholders.
        widgets = {
            'proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'telefono': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Número de teléfono'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección'}),
        }
        
    #Validación personalizada: Aseguramos que el correo termine en @gmail.com.
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if not correo.endswith('@gmail.com'):
            raise forms.ValidationError("El correo debe ser de dominio @gmail.com.")
        return correo

