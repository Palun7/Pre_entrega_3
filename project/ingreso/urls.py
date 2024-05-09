from django.urls import path
from ingreso.views import index, registro_index, ingreso, registro, egreso, listausuarios

app_name = "ingreso"

urlpatterns = [
    path("", index, name = "index"),
    path("registro_index", registro_index, name = "registro_index"),
    path("ingreso/acceder", ingreso, name= "acceder"),
    path("ingreso/registro", registro, name= "registro"),
    path("ingreso/egreso", egreso, name="egreso"),
    path("ingreso/lista_usuarios", listausuarios, name='lista_usuarios')
]