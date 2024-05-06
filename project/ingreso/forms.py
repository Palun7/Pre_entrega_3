from django import forms
from ingreso.models import Ingreso, Usuario, Egreso

class FormIngreso(forms.ModelForm):

    class Meta:
        model = Ingreso
        fields = '__all__'

class FormUsuario(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = '__all__'

class FormEgreso(forms.ModelForm):
    
    class Meta:
        model = Egreso
        fields = '__all__'