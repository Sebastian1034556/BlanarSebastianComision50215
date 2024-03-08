from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,"aplicacion/index.html")

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request,"aplicacion/about.html",contexto)


def empleados(request):
    return render(request,"aplicacion/store.html")

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
    else:
        miForm = ClienteForm()
        
    return render(request,"aplicacion/clienteForm.html",{"form": miForm})