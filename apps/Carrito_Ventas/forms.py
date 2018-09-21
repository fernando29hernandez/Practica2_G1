from django.forms import ModelForm, Textarea, TextInput, URLInput
from apps.Carrito_Ventas.models import Seccion
from apps.Carrito_Ventas.models import Articulo
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe

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