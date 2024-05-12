from django.shortcuts import render, redirect
from ventas.forms import NuevoClienteForm, LocalidadForm, PaisForm, NuevoProductoForm, MarcaForm, VentaForm
from ventas.models import Venta, NuevoCliente, NuevoProducto
from django.db.models import Q

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

def pais(request):
    if request.method == 'POST':
        form_pais = PaisForm(request.POST)
        if form_pais.is_valid():
            form_pais.save()
            return redirect('ventas:index')
    else:
        form_pais = PaisForm()
    return render(request, 'ventas/pais.html', {'form_pais': form_pais})

def nuevoproducto(request):
    if request.method == 'POST':
        form_producto = NuevoProductoForm(request.POST)
        if form_producto.is_valid():
            form_producto.save()
            return redirect('ventas:index')
    else:
        form_producto = NuevoProductoForm()
    return render(request, 'ventas/nuevo_producto.html', {'form_producto': form_producto})

def marca(request):
    if request.method == 'POST':
        form_marca = MarcaForm(request.POST)
        if form_marca.is_valid():
            form_marca.save()
            return redirect('ventas:nuevo_producto')
    else:
        form_marca = MarcaForm()
    return render(request, 'ventas/marca.html', {'form_marca': form_marca})

def venta(request):
    if request.method == 'POST':
        form_venta = VentaForm(request.POST)
        if form_venta.is_valid():
            form_venta.save()
            return redirect('ventas:index')
    else:
        form_venta = VentaForm()
    return render(request, 'ventas/venta.html', {'form_venta': form_venta})

def listaventas(request):
    lista_ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'lista_ventas': lista_ventas})

def listaclientes(request):
    busqueda = request.GET.get('busqueda', None)
    consulta = NuevoCliente.objects.all()
    if busqueda:
        consulta = NuevoCliente.objects.filter(Q(nombre__icontains=busqueda)|Q(dni__icontains=busqueda)|Q(direccion__icontains=busqueda)|Q(localidad__localidad__icontains=busqueda))
    else:
        consulta = NuevoCliente.objects.all()
    return render(request, 'ventas/lista_clientes.html', {'lista_clientes': consulta})

def listaproductos(request):
    lista_productos = NuevoProducto.objects.all()
    return render(request, 'ventas/lista_productos.html', {'lista_productos': lista_productos})

def cambiarprecio(request, pk):
    consulta = NuevoProducto.objects.get(id=pk)
    if request.method == "POST":
        form_precio = NuevoProductoForm(request.POST, instance=consulta)
        if form_precio.is_valid():
            form_precio.save()
            return redirect("ventas:venta")
    else:
        form_precio = NuevoProductoForm(instance=consulta)
    return render(request, "ventas/cambiar_precio.html", {"form_precio": form_precio})

