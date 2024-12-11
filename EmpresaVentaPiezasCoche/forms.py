# Importamos las clases necesarias de Django
from django import forms
from django.forms import ModelForm
from .models import Proveedor  # Asegúrate de que el modelo Proveedor esté importado

#crear un proveedor
# Definimos un formulario basado en el modelo Proveedor
""""


class ProveedorModelForm(ModelForm):
    # Clase interna Meta para definir configuraciones del formulario
    class Meta:
        model = Proveedor  # Especificamos que este formulario está basado en el modelo Proveedor
        fields = ['proveedor', 'telefono', 'correo', 'direccion']  # Campos que queremos incluir en el formulario
        labels = {  # Etiquetas personalizadas para los campos
            'proveedor': 'Nombre del Proveedor',  # Etiqueta para el campo 'proveedor'
            'telefono': 'Teléfono de Contacto',  # Etiqueta para el campo 'telefono'
            'correo': 'Correo Electrónico',  # Etiqueta para el campo 'correo'
            'direccion': 'Dirección del Proveedor',  # Etiqueta para el campo 'direccion'
        }
        help_texts = {  # Textos de ayuda que se mostrarán junto a los campos
            'correo': 'Asegúrate de ingresar un correo único.',  # Ayuda para el campo 'correo'
        }
        widgets = {  # Personalización de los widgets (elementos HTML) de los campos
            'direccion': forms.Textarea(attrs={'rows': 3, 'cols': 50}),  # Campo 'direccion' como un área de texto
        }

    # Método para limpiar y validar los datos del formulario
    def clean(self):
        super().clean()  # Llamamos al método clean de la clase padre para asegurarnos de que se realicen las validaciones básicas

        # Validar que el nombre del proveedor sea único
        proveedor = self.cleaned_data.get('proveedor')  # Obtenemos el valor del campo 'proveedor'
        proveedor_existente = Proveedor.objects.filter(proveedor=proveedor).first()  # Buscamos si ya existe un proveedor con ese nombre
        # Si existe y no es el mismo que estamos editando, agregamos un error
        if proveedor_existente and (not self.instance or proveedor_existente.id != self.instance.id):
            self.add_error('proveedor', 'Ya existe un proveedor con este nombre.')  # Mensaje de error para el campo 'proveedor'

        # Validar que el correo sea único
        correo = self.cleaned_data.get('correo')  # Obtenemos el valor del campo 'correo'
        correo_existente = Proveedor.objects.filter(correo=correo).first()  # Buscamos si ya existe un proveedor con ese correo
        # Si existe y no es el mismo que estamos editando, agregamos un error
        if correo_existente and (not self.instance or correo_existente.id != self.instance.id):
            self.add_error('correo', 'Ya existe un proveedor con este correo.')  # Mensaje de error para el campo 'correo'

        # Validar que el número de teléfono tenga un formato válido (por ejemplo, 10 dígitos)
        telefono = self.cleaned_data.get('telefono')  # Obtenemos el valor del campo 'telefono'
        # Comprobamos que el teléfono tenga al menos 7 dígitos y que solo contenga números
        if len(telefono) < 7 or not telefono.isdigit():
            self.add_error('telefono', 'El número de teléfono debe tener al menos 7 dígitos y ser numérico.')  # Mensaje de error para el campo 'telefono'

        return self.cleaned_data  # Devolvemos los datos limpios y validados
    
#realizar una busqueda avanzada
class BusquedaAvanzadaProveedorForm(forms.Form):
    nombre_proveedor = forms.CharField(required=False, label="Nombre del Proveedor")
    correo = forms.EmailField(required=False, label="Correo Electrónico")
    telefono = forms.CharField(required=False, label="Teléfono")

    def clean(self):
        super().clean()
        
        # Obtenemos los campos
        nombre_proveedor = self.cleaned_data.get('nombre_proveedor')
        correo = self.cleaned_data.get('correo')
        telefono = self.cleaned_data.get('telefono')

        # Controlamos que al menos un campo tenga un valor
        if not nombre_proveedor and not correo and not telefono:
            self.add_error(None, 'Debe introducir al menos un valor en un campo del formulario')

        return self.cleaned_data
        
"""

class ProveedorModelForm(ModelForm):   
    class Meta:

        model = Proveedor
        fields = ['proveedor','telefono','correo','direccion']
        labels = {
            "proveedor": ("Nombre del proveedor hola"),
        }
        help_texts = {
            "proveedor": ("200 caracteres como máximo"),
           
        }
        #
        #widgets = {
        #    "fecha_publicacion":forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        #}
        #localized_fields = ["fecha_publicacion"]
    
    
    def clean(self):
 
        #Validamos con el modelo actual
        super().clean()
        
        #Obtenemos los campos 
        proveedor = self.cleaned_data.get('proveedor')
        telefono = self.cleaned_data.get('telefono')
        correo = self.cleaned_data.get('correo')
        direccion = self.cleaned_data.get('direccion')
      
 
        #Comprobamos que no exista un proveedor con ese nombre
        proveedorNombre = Proveedor.objects.filter(proveedor=proveedor).first()
        if(not proveedorNombre is None
           ):
             if(not self.instance is None and proveedorNombre.id == self.instance.id):
                 pass
             else:
                self.add_error('proveedor','Ya existe un proveedor con ese nombre')


                
        #Siempre devolvemos el conjunto de datos.
        return self.cleaned_data