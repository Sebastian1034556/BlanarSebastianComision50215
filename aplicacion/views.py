from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
def home(request):
    return render(request,"aplicacion/index.html")

def store(request):
    return render(request,"aplicacion/store.html")

def about(request):
    return render(request,"aplicacion/about.html")

#-----------------------------------------------CLIENTES------------------------------------------------------------------------

#------------------------------------------------CREATE------------------------------------------------------------------------
@login_required
def clienteCreate(request):
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
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm()
        return render(request,"aplicacion/clientes.html",{"form": miForm}) 

#-------------------------------------------------READ----------------------------------------------------------------------------------------
@login_required
def clientes(request):
    formulario_cliente = ClienteForm()
    contexto = {
        'clientes': Cliente.objects.all(),
        'form': formulario_cliente
    }
    return render(request,"aplicacion/clientes.html",contexto)

#-------------------------------------------------UPDATE----------------------------------------------------------------------------------------
@login_required
def clienteUpdate(request,id_cliente):
    cliente = Cliente.objects.get(id = id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.apellido = miForm.cleaned_data.get("apellido")
            cliente.edad =  miForm.cleaned_data.get("edad")
            cliente.dni = miForm.cleaned_data.get("dni")
            cliente.save()
            
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm(initial={'nombre': cliente.nombre, 'apellido' : cliente.apellido, 'edad' : cliente.edad , 'dni' : cliente.dni} )
    return render(request,"aplicacion/clienteForm.html",{"form": miForm}) 

#-------------------------------------------------DELETE----------------------------------------------------------------------------------------
@login_required
def clienteDelete(request,id_cliente):
    cliente = Cliente.objects.get(id = id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))
#------------------------------------------------EMPLEADOS------------------------------------------------------------------------

#------------------------------------------------CREATE------------------------------------------------------------------------
@login_required
def empleadoCreate(request):
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
            return redirect(reverse_lazy('empleados'))
    else:
        miForm = EmpleadoForm()
        return render(request,"aplicacion/empleados.html",{"form": miForm}) 

#--------------------------------------------------READ-------------------------------------------------------------------------------
@login_required
def empleados(request):
    formulario_empleado = EmpleadoForm()
    contexto = {
        'empleados': Empleado.objects.all(),
        'form': formulario_empleado
    }
    return render(request,"aplicacion/empleados.html",contexto)
#-------------------------------------------------UPDATE----------------------------------------------------------------------------------------
@login_required
def empleadoUpdate(request,id_empleado):
    empleado = Empleado.objects.get(id = id_empleado)
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            empleado.nombre = miForm.cleaned_data.get("nombre")
            empleado.apellido = miForm.cleaned_data.get("apellido")
            empleado.edad =  miForm.cleaned_data.get("edad")
            empleado.dni = miForm.cleaned_data.get("dni")
            empleado.sueldo = miForm.cleaned_data.get("sueldo")
            empleado.save()
            
            return redirect(reverse_lazy('empleados'))
    else:
        miForm = EmpleadoForm(initial={'nombre': empleado.nombre, 'apellido' : empleado.apellido, 'edad' : empleado.edad , 'dni' : empleado.dni , 'sueldo': empleado.sueldo} )
    return render(request,"aplicacion/empleadoForm.html",{"form": miForm})

#-------------------------------------------------DELETE----------------------------------------------------------------------------------------
@login_required
def empleadoDelete(request,id_empleado):
    empleado = Empleado.objects.get(id = id_empleado)
    empleado.delete()
    return redirect(reverse_lazy('empleados'))
#-----------------------------------------------PRODUCTOS------------------------------------------------------------------------

#------------------------------------------------CREATE------------------------------------------------------------------------
@login_required
def productoCreate(request):
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
            return redirect(reverse_lazy('productos'))
    else:
        miForm = ProductoForm()
        return render(request,"aplicacion/productos.html",{"form": miForm})

#--------------------------------------------------READ-----------------------------------------------------------------------------------
@login_required
def productos(request):
    formulario_producto = ProductoForm()
    contexto = {
        'productos': Producto.objects.all(),
        'form': formulario_producto
    }
    return render(request,"aplicacion/productos.html",contexto)

#----------------------------------------------------------UPDATE---------------------------------------------------------------------------
@login_required
def productoUpdate(request,id_producto):
    producto = Producto.objects.get(id = id_producto)
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto.nombre = miForm.cleaned_data.get("nombre")
            producto.precio = miForm.cleaned_data.get("precio")
            producto.marca =  miForm.cleaned_data.get("marca")
            producto.stock = miForm.cleaned_data.get("stock")
            producto.color = miForm.cleaned_data.get("color")
            producto.talla = miForm.cleaned_data.get("talla")
            
            producto.save()
            
            return redirect(reverse_lazy('productos'))
    else:
        miForm = ProductoForm(initial={'nombre': producto.nombre, 'precio' : producto.precio, 'marca' : producto.marca ,'stock' : producto.stock, 'color' : producto.color , 'talla': producto.talla} )
    return render(request,"aplicacion/productoForm.html",{"form": miForm})

#----------------------------------------------------------DELETE---------------------------------------------------------------------------
@login_required
def productoDelete(request,id_producto):
    producto = Producto.objects.get(id = id_producto)
    producto.delete()
    return redirect(reverse_lazy('productos'))

#-------------------------------------------------------BUSCAR-----------------------------------------------------------------------------
@login_required
def buscarClientes(request):
    return render(request,"aplicacion/buscar.html")

@login_required
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

@login_required
def buscarEmpleados(request):
    return render(request,"aplicacion/buscar.html")

@login_required
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


@login_required
def buscarProductos(request):
    return render(request,"aplicacion/buscar.html")

@login_required
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



#------------------------------------------LOGIN, LOGOUT, AUTHENTICATION, REGISTRATION-------------------------------------------------------
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave= request.POST['password']
        user = authenticate(request, username = usuario, password = clave)
        if user is not None:
            login(request, user)
            
            #__________Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #________________________________________________________
            return render(request, 'aplicacion/index.html')
        else: 
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    
    return render(request,"aplicacion/login.html",{"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
    
    return render(request,"aplicacion/registro.html",{"form": miForm})

#------------------------------------------EDICIÓN DE PERFIL, CAMBIO DE CLAVE, AVATAR,-------------------------------------------------------
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)

        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)
    
    return render(request,"aplicacion/editarPerfil.html",{"form": miForm})

class CambiarClave(LoginRequiredMixin,PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #____ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()
    
    return render(request,"aplicacion/agregarAvatar.html",{"form": miForm})