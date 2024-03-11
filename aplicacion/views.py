from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,"aplicacion/index.html")

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request,"aplicacion/clientes.html",contexto)

def empleados(request):
    return render(request,"aplicacion/empleados.html")

def store(request):
    return render(request,"aplicacion/store.html")

def about(request):
    return render(request,"aplicacion/about.html")

def productos(request):
    return render(request,"aplicacion/products.html")

#-----------------------------------------------Form
def clienteForm(request):
    if request.method == "POST":
        #Si es la 2da vez o más
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_edad =  miForm.cleaned_data.get("edad")
            cliente_dni = miForm.cleaned_data.get("dni")
            cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido, edad = cliente_edad,dni = cliente_dni)
            cliente.save()
            contexto = {'clientes': Cliente.objects.all()}
            return render(request,"aplicacion/clientes.html",contexto)
    else:
        miForm = ClienteForm()
        return render(request,"aplicacion/clienteForm.html",{"form": miForm}) 
    
def empleadoForm(request):
    if request.method == "POST":
        #Si es la 2da vez o más
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            empleado_nombre = miForm.cleaned_data.get("nombre")
            empleado_apellido = miForm.cleaned_data.get("apellido")
            empleado_edad =  miForm.cleaned_data.get("edad")
            empleado_dni = miForm.cleaned_data.get("dni")
            empleado_sueldo = miForm.cleaned_data.get("sueldo")
            empleado = Empleado(nombre = empleado_nombre, apellido = empleado_apellido, edad = empleado_edad,dni = empleado_dni, sueldo = empleado_sueldo)
            empleado.save()
            contexto = {'empleados': Empleado.objects.all()}
            return render(request,"aplicacion/empleados.html",contexto)
    else:
        miForm = EmpleadoForm()
        return render(request,"aplicacion/empleadoForm.html",{"form": miForm}) 
    
def buscarClientes(request):
    return render(request,"aplicacion/buscar.html")

def encontrarClientes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = { "clientes" : clientes }
        return render(request,"aplicacion/clientes.html",contexto)
    
    contexto = {'clientes': Cliente.objects.all()}
    return render(request,"aplicacion/clientes.html",contexto)