from django.urls import path
from ventas.views import index, nuevocliente, localidad

app_name = 'ventas'

urlpatterns = [
    path('ventas/index', index, name='index'),
    path('ventas/nuevo_cliente', nuevocliente, name='nuevocliente'),
    path('ventas/localidad', localidad, name='localidad')
]