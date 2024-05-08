from django.shortcuts import render, redirect
from ventas.forms import NuevoClienteForm, LocalidadForm

def index(request):
    return render(request, 'ventas/index.html')

def nuevocliente(request):
    if request.method == 'POST':
        form_cliente = NuevoClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('ventas:index')
    else:
        form_cliente = NuevoClienteForm()
    return render(request, 'ventas/nuevo_cliente.html', {'form_cliente': form_cliente})

def localidad(request):
    if request.method == 'POST':
        form_localidad = LocalidadForm(request.POST)
        if form_localidad.is_valid():
            form_localidad.save()
            return redirect('ventas:nuevocliente')
    else:
        form_localidad = LocalidadForm()
    return render(request, 'ventas/localidad.html', {'form_localidad': form_localidad})