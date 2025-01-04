from django import forms
from .models import Producto, Fabricante

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class ProductoForm(forms.ModelForm):
    # El campo país debe estar fuera de Meta
    pais = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese país del fabricante',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'fabricante', 'f_vencimiento']
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre del producto',
                'autocomplete': 'off',
                'required': True
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese descripción breve',
                'autocomplete': 'off'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
                'placeholder': '0.00',
                'required': True
            }),
            'fabricante': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'f_vencimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            })
        }

        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio ($)',
            'fabricante': 'Fabricante',
            'f_vencimiento': 'Fecha de Vencimiento'
        }

        error_messages = {
            'nombre': {
                'required': 'El nombre del producto es obligatorio',
                'max_length': 'El nombre no puede exceder los 100 caracteres'
            },
            'precio': {
                'required': 'El precio es obligatorio',
                'invalid': 'Por favor ingrese un precio válido'
            },
            'f_vencimiento': {
                'required': 'La fecha de vencimiento es obligatoria',
                'invalid': 'Por favor ingrese una fecha válida'
            }
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que 0')
        return precio

    def clean_f_vencimiento(self):
        fecha = self.cleaned_data.get('f_vencimiento')
        if not fecha:
            raise forms.ValidationError('La fecha de vencimiento es obligatoria')
        return fecha

    def save(self, commit=True):
        producto = super().save(commit=False)
        if commit:
            fabricante = producto.fabricante
            fabricante.pais = self.cleaned_data.get('pais')
            fabricante.save()
            producto.save()
        return producto
    

# Formulario para crear un nuevo usuario
class RegisterForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

