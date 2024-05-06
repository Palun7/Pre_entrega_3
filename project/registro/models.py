from django.db import models

class RegistroUsuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    puesto = models.CharField(max_length=50, verbose_name='Puesto')
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"