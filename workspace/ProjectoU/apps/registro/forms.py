from django import forms

from .models import Registro
class PostForm(forms.ModelForm):
   
    class Meta:
        
        model = Registro
        fields = ('rut', 'razon_social', 'correo', 'listado_docuemento', 'fecha_registro')