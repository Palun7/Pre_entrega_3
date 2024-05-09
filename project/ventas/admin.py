from django.contrib import admin
from ventas.models import NuevoCliente, Localidad, Pais, NuevoProducto, Venta, Marca

admin.site.register(NuevoCliente)
admin.site.register(Localidad)
admin.site.register(Pais)
admin.site.register(NuevoProducto)
admin.site.register(Venta)
admin.site.register(Marca)

