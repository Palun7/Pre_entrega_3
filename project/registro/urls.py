from django.urls import path
from registro.views import index, registro

app_name = 'registro'

urlpatterns = [
    path('', index, name= 'index'),
    path('registro_usuarios/', registro, name= 'registro'),
]