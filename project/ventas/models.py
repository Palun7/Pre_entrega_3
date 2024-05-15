from django.db import models
from django.core.validators import RegexValidator
from ingreso.models import Usuario

class Pais(models.Model):
    pais = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Ese pais ya existe en el sistema.'}, verbose_name='país')

    def __str__(self):
        return self.pais

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

class Localidad(models.Model):
    localidad = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Esa ciudad ya existe en el sistema.'})
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.localidad

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Esa marca ya esta registrada.'}, verbose_name='Nombre de la marca')
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True, verbose_name='País de origen')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class NuevoCliente(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=8,validators=[RegexValidator(r'^\d{7,8}$', 'Ingrese un máximo de 8 dígitos.')], unique=True, error_messages={'unique': 'El DNI debe ir sin puntos'}, verbose_name='DNI')
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}, DNI: {self.dni}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class NuevoProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True, error_messages={'unique': 'Ese producto ya esta registrado.'}, verbose_name='Nombre del producto')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Marca del producto')
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.marca}, {self.nombre}: ${self.precio}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Venta(models.Model):
    producto = models.ForeignKey(NuevoProducto, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(NuevoCliente, on_delete=models.SET_NULL, null=True, blank=True)
    vendedor = models.ForeignKey(Usuario,on_delete=models.SET_NULL, null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra: {self.producto}. Cliente: {self.cliente}. Vendedor: {self.vendedor}. Fecha: {self.fecha_hora}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
