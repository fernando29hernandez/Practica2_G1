
# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe

from django.forms import ModelForm, Textarea, TextInput, URLInput, PasswordInput, EmailInput
from apps.Carrito_Ventas.models import Seccion, Usuario, Articulo

class SeccionForm(ModelForm):
    class Meta:
        model = Seccion
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
            'descripcion': TextInput(attrs={'class':'form-control'}),
            
        }

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'descripcion', 'precio', 'seccion_fk', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'seccion_fk': forms.Select(attrs={'class':'form-control','maxlength':'60'}),
            'imagen': forms.FileInput(),
        }
        labels={
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
            'seccion_fk': 'Seccion',
            'imagen': 'Imagen',
        }
    def __init__(self, *args, **kwargs): 
        super(ArticuloForm, self).__init__(*args, **kwargs) 
        self.fields['imagen'].required = False

class CrearUsuarioForm(ModelForm):
     class Meta:
         model = Usuario
         fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
         ]
         labels = {
            'username':'Nombre de usuario',
            'password':'Contraseña',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo electrónico',
         }
         widgets = {
            'username':TextInput(attrs={'class':'form-control'}),
            'password':PasswordInput(attrs={'class':'form-control'}),
            'first_name':TextInput(attrs={'class':'form-control'}),
            'last_name':TextInput(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
         }

class CrearUsuarioTipoForm(ModelForm):
     class Meta:
         model = Usuario
         fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'tipo',
         ]
         labels = {
            'username':'Nombre de usuario',
            'password':'Contraseña',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo electrónico',
            'tipo':'Tipo de usuario(check=Admin or Usuario)',
         }
         widgets = {
            'username':TextInput(attrs={'class':'form-control'}),
            'password':PasswordInput(attrs={'class':'form-control'}),
            'first_name':TextInput(attrs={'class':'form-control'}),
            'last_name':TextInput(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
         }