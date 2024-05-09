from django.contrib import admin
from ventas.models import NuevoCliente, Localidad, Pais, NuevoProducto

admin.site.register(NuevoCliente)
admin.site.register(Localidad)
admin.site.register(Pais)
admin.site.register(NuevoProducto)
