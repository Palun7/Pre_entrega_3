from django import forms
from ventas.models import NuevoCliente, Localidad, Pais, NuevoProducto, Marca

class NuevoClienteForm(forms.ModelForm):

    class Meta:
        model = NuevoCliente
        fields = '__all__'

class LocalidadForm(forms.ModelForm):

    class Meta:
        model = Localidad
        fields = '__all__'

class PaisForm(forms.ModelForm):

    class Meta:
        model = Pais
        fields = '__all__'

class NuevoProductoForm(forms.ModelForm):

    class Meta:
        model = NuevoProducto
        fields = '__all__'

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'