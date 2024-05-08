from django import forms
from ventas.models import NuevoCliente, Localidad

class NuevoClienteForm(forms.ModelForm):

    class Meta:
        model = NuevoCliente
        fields = '__all__'

class LocalidadForm(forms.ModelForm):
    
    class Meta:
        model = Localidad
        fields = '__all__'