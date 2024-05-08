from django.db import models
from django.core.validators import RegexValidator

class Localidad(models.Model):
    localidad = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Esa ciudad ya existe en el sistema.'})
    
    def __str__(self):
        return self.localidad
    
    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

class NuevoCliente(models.Model):
    nombre = models.CharField(max_length=50)
    DNI = models.CharField(max_length=8,validators=[RegexValidator(r'^\d{7,8}$', 'Ingrese un máximo de 8 dígitos.')], unique=True, error_messages={'unique': 'El DNI debe ir sin puntos'})
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre}, DNI: {self.DNI}'
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'