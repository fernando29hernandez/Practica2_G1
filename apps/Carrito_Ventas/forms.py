from django.forms import ModelForm, Textarea, TextInput, URLInput
from apps.Carrito_Ventas.models import Seccion
class SeccionForm(ModelForm):
    class Meta:
        model = Seccion
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
            'descripcion': TextInput(attrs={'class':'form-control'}),
            
        }