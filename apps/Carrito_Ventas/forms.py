# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, TextInput, URLInput, PasswordInput, EmailInput
from apps.Carrito_Ventas.models import Seccion, Usuario

class SeccionForm(ModelForm):
    class Meta:
        model = Seccion
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
            'descripcion': TextInput(attrs={'class':'form-control'}),
            
        }


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