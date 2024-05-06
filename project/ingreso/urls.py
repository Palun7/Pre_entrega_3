from django.urls import path
from ingreso.views import index, ingreso, registro, egreso

app_name = "ingreso"

urlpatterns = [
    path("", index, name = "index"),
    path("ingreso/acceder.html", ingreso, name= "acceder"),
    path("ingreso/registro.html", registro, name= "registro"),
    path("ingreso/egreso.html", egreso, name="egreso"),
]