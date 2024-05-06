from django.shortcuts import render, redirect
from registro.forms import FormUsuario

def index(request):
    return render(request, "registro/index.html")

def registro(request):
    if request.method == 'POST':
        form_registro = FormUsuario(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            return redirect('../')
    else:
        form_registro = FormUsuario()
    return render(request, 'registro/registro.html', {'form_registro': form_registro})
