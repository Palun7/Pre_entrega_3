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

class Pais(models.Model):
    pais = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Ese pais ya existe en el sistema.'})

    def __str__(self):
        return self.pais

    class Meta:
        verbose_name = 'Paises'
        verbose_name_plural = 'Paises'

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Esa marca ya esta registrada.'})
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class NuevoProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Ese producto ya esta registrado.'})
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}: ${self.precio}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'