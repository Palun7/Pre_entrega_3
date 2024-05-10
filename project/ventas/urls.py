from django.urls import path
from ventas.views import index, nuevocliente, localidad, pais, nuevoproducto, marca, venta, listaventas, listaclientes, listaproductos, cambiarprecio

app_name = 'ventas'

urlpatterns = [
    path('ventas/index', index, name='index'),
    path('ventas/nuevo_cliente', nuevocliente, name='nuevocliente'),
    path('ventas/localidad', localidad, name='localidad'),
    path('ventas/pais', pais, name='pais'),
    path('ventas/nuevoproducto', nuevoproducto, name='nuevo_producto'),
    path('ventas/marca', marca, name='marca'),
    path('ventas/venta', venta, name='venta'),
    path('ventas/lista_ventas', listaventas, name='lista_ventas'),
    path('ventas/lista_clientes', listaclientes, name='lista_clientes'),
    path('ventas/lista_productos', listaproductos, name='lista_productos'),
    path('ventas/cambiar_precio/<int:pk>', cambiarprecio, name='cambiar_precio'),
]