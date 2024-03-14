from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,"aplicacion/index.html")

def store(request):
    return render(request,"aplicacion/store.html")

def about(request):
    return render(request,"aplicacion/about.html")

#-----------------------------------------------CLIENTES------------------------------------------------------------------------

#------------------------------------------------CREATE------------------------------------------------------------------------
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
            return redirect('clientes')
    else:
        miForm = ClienteForm()
        return render(request,"aplicacion/clientes.html",{"form": miForm}) 

#-------------------------------------------------READ----------------------------------------------------------------------------------------
def clientes(request):
    formulario_cliente = ClienteForm()
    contexto = {
        'clientes': Cliente.objects.all(),
        'form': formulario_cliente
    }
    return render(request,"aplicacion/clientes.html",contexto)
#------------------------------------------------EMPLEADOS------------------------------------------------------------------------

#------------------------------------------------CREATE------------------------------------------------------------------------
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
            return redirect('empleados')
    else:
        miForm = EmpleadoForm()
        return render(request,"aplicacion/empleados.html",{"form": miForm}) 




#--------------------------------------------------READ-------------------------------------------------------------------------------
def empleados(request):
    formulario_empleado = EmpleadoForm()
    contexto = {
        'empleados': Empleado.objects.all(),
        'form': formulario_empleado
    }
    return render(request,"aplicacion/empleados.html",contexto)

#-----------------------------------------------PRODUCTOS------------------------------------------------------------------------

#------------------------------------------------CREATE------------------------------------------------------------------------
def productoForm(request):
    if request.method == "POST":
        #Si es la 2da vez o más
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_precio = miForm.cleaned_data.get("precio")
            producto_marca =  miForm.cleaned_data.get("marca")
            producto_stock =  miForm.cleaned_data.get("stock")
            producto_color = miForm.cleaned_data.get("color")
            producto_talla = miForm.cleaned_data.get("talla")
            producto = Producto(nombre = producto_nombre, precio = producto_precio, stock = producto_stock,marca = producto_marca,color = producto_color, talla = producto_talla)
            producto.save()
            return redirect('productos')
    else:
        miForm = ProductoForm()
        return render(request,"aplicacion/productos.html",{"form": miForm})

#--------------------------------------------------READ-----------------------------------------------------------------------------------
def productos(request):
    formulario_producto = ProductoForm()
    contexto = {
        'productos': Producto.objects.all(),
        'form': formulario_producto
    }
    return render(request,"aplicacion/productos.html",contexto)

#------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------BUSCAR-----------------------------------------------------------------------------
def buscarClientes(request):
    return render(request,"aplicacion/buscar.html")


def encontrarClientes(request):
    patron = request.GET.get("buscar")
    if patron:
        clientes = Cliente.objects.filter(            
            Q(nombre__icontains=patron) |
            Q(apellido__icontains=patron) |
            Q(id__icontains=patron) |
            Q(edad__icontains=patron)|
            Q(dni__icontains=patron)
)
    else:
        clientes = Cliente.objects.all()
    
    contexto = {"clientes": clientes}
    return render(request, "aplicacion/clientes.html", contexto)


def buscarEmpleados(request):
    return render(request,"aplicacion/buscar.html")

def encontrarEmpleados(request):
    patron = request.GET.get("buscar")
    if patron:
        empleados = Empleado.objects.filter(            
            Q(nombre__icontains=patron) |
            Q(apellido__icontains=patron) |
            Q(id__icontains=patron) |
            Q(edad__icontains=patron) |
            Q(sueldo__icontains=patron) |
            Q(dni__icontains=patron)
)
    else:
        empleados = Empleado.objects.all()
    
    contexto = {"empleados": empleados}
    return render(request, "aplicacion/empleados.html", contexto)



def buscarProductos(request):
    return render(request,"aplicacion/buscar.html")

def encontrarProductos(request):
    patron = request.GET.get("buscar")
    if patron:
        productos = Producto.objects.filter(            
            Q(nombre__icontains=patron) |
            Q(precio__icontains=patron) |
            Q(marca__icontains=patron) |
            Q(stock__icontains=patron) |
            Q(color__icontains=patron) |
            Q(talla__icontains=patron)
)
    else:
        productos = Producto.objects.all()
    
    contexto = {"productos": productos}
    return render(request, "aplicacion/productos.html", contexto)