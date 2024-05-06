from django.shortcuts import render,redirect
from ingreso.forms import FormIngreso, FormUsuario, FormEgreso

def index(request):
    return render(request, 'ingreso/index.html')

def ingreso(request):
    if request.method == 'POST':
        form_ingreso = FormIngreso(request.POST)
        if form_ingreso.is_valid():
            form_ingreso.save()
            return redirect('../') 
    else:
        form_ingreso = FormIngreso()
    return render(request, 'ingreso/acceder.html', {'form_ingreso': form_ingreso})

def registro(request):
    if request.method == 'POST':
        form_registro = FormUsuario(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            return redirect('../')
    else:
        form_registro = FormUsuario()
    return render(request, 'ingreso/registro.html', {'form_registro': form_registro})

def egreso(request):
    if request.method == 'POST':
        form_egreso = FormEgreso(request.POST)
        if form_egreso.is_valid():
            form_egreso.save()
            return redirect('../')
    else:
        form_egreso = FormEgreso()
    return render(request, 'ingreso/egreso.html', {'form_egreso': form_egreso})
