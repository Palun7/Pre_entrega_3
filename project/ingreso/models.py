from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    puesto = models.CharField(max_length=50, verbose_name='Puesto')
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Ingreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Entrada de usuario")
    ingreso = models.DateTimeField(auto_now_add=True, verbose_name='Hora de entrada')

    def __str__(self):
        return f'{self.usuario}, {self.ingreso}'

    class Meta:
        verbose_name = "Acceso"
        verbose_name_plural = "Accesos"

class Egreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Salida de usuario" )
    egreso = models.DateTimeField(auto_now_add=True, verbose_name='Hora de salida')
    
    def __str__(self):
        return f'{self.usuario}, {self.egreso}'
    
    class Meta:
        verbose_name = "Egreso"
        verbose_name_plural = "Egresos"
