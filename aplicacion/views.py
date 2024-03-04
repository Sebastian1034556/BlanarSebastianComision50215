from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"aplicacion/index.html")

def clientes(request):
    return render(request,"aplicacion/about.html")


def empleados(request):
    return render(request,"aplicacion/store.html")

def productos(request):
    return render(request,"aplicacion/products.html")

