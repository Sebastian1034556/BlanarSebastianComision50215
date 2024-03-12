from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,"aplicacion/index.html")

def clientes(request):
    formulario_cliente = ClienteForm()
    contexto = {
        'clientes': Cliente.objects.all(),
        'form': formulario_cliente
    }
    return render(request,"aplicacion/clientes.html",contexto)

def empleados(request):
    formulario_empleado = EmpleadoForm()
    contexto = {
        'empleados': Empleado.objects.all(),
        'form': formulario_empleado
    }
    return render(request,"aplicacion/empleados.html",contexto)

# def login(request):
#     formulario_cliente = LoginForm()
#     contexto = {'form': formulario_cliente}
#     return render(request,"aplicacion/login.html",contexto)

def store(request):
    return render(request,"aplicacion/store.html")

def about(request):
    return render(request,"aplicacion/about.html")

def productos(request):
    formulario_producto = ProductoForm()
    contexto = {
        'productos': Producto.objects.all(),
        'form': formulario_producto
    }
    return render(request,"aplicacion/productos.html",contexto)

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
            return redirect('clientes')
    else:
        miForm = ClienteForm()
        return render(request,"aplicacion/clientes.html",{"form": miForm}) 
    
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
    
# def loginForm(request):
#     if request.method == "POST":
#         #Si es la 2da vez o más
#         miForm = LoginForm(request.POST)
#         if miForm.is_valid():
#             login_usuario = miForm.cleaned_data.get("usuario")
#             login_contraseña = miForm.cleaned_data.get("contraseña")
#             login = Login(usuario = login_usuario, contraseña = login_contraseña)
#             login.save()
#             contexto = {'login': Login.objects.all()}
#             return render(request,"aplicacion/login.html",contexto)
#     else:
#         miForm = loginForm()
#         return render(request,"aplicacion/login.html",{"form": miForm}) 
    
    
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