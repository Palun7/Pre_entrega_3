from django.contrib import admin
from ventas.models import NuevoCliente, Localidad, Pais, NuevoProducto, Venta

admin.site.register(NuevoCliente)
admin.site.register(Localidad)
admin.site.register(Pais)
admin.site.register(NuevoProducto)
admin.site.register(Venta)

