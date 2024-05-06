from django import forms
from registro.models import RegistroUsuario

class FormUsuario(forms.ModelForm):
    
    class Meta:
        model = RegistroUsuario
        fields = '__all__'