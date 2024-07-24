from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"aplicacion/index.html")

def store(request):
    return render(request,"aplicacion/store.html")

def checkout(request):
    return render(request,"aplicacion/checkout.html")
#-------------------------------------------------------CRUD-------------------------------------------------------------------------
#region CRUD
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
            
            if not isinstance(cliente_dni,int) or cliente_dni > 99999999:
                return JsonResponse({'error': 'El DNI debe ser un número de 8 dígitos'}, status=400)
                
            else:
                cliente.save()
                messages.add_message(request=request,level=messages.SUCCESS,message="Cliente agregado con éxito")
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
def clienteDelete(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        if 'confirmar' in request.POST:
            cliente.delete()
            messages.success(request, f"El cliente '{cliente.nombre}' ha sido eliminado exitosamente.")
        return redirect('clientes')
    return render(request, 'aplicacion/cliente_delete.html', {'cliente': cliente})

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
            messages.add_message(request=request,level=messages.SUCCESS,message="Empleado agregado con éxito")
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
    empleado = Empleado.objects.get(id=id_empleado)
    if request.method == 'POST':
        if 'confirmar' in request.POST:
            empleado.delete()
            messages.success(request, f"El empleado '{empleado.nombre}' ha sido eliminado exitosamente.")
        return redirect('empleados')
    return render(request, 'aplicacion/empleado_delete.html', {'empleado': empleado})

#-----------------------------------------------PRODUCTOS----------------------------------------------------------------

#------------------------------------------------CREATE------------------------------------------------------------------
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
            messages.add_message(request=request,level=messages.SUCCESS,message="Producto agregado con éxito")
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

#----------------------------------------------------------DELETE----------------------------------------------------------------------
@login_required
def productoDelete(request,id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        if 'confirmar' in request.POST:
            producto.delete()
            messages.success(request, f"El producto '{producto.nombre}' ha sido eliminado exitosamente.")
        return redirect('productos')
    return render(request, 'aplicacion/producto_delete.html', {'producto': producto})
#----------------------------------------------------------PEDIDO----------------------------------------------------------------------
#----------------------------------------------------------CREATE----------------------------------------------------------------------
@login_required
def pedidoCreate(request):
    if request.method == "POST":
        #Si es la 2da vez o más
        miForm = PedidoForm(request.POST)
        if miForm.is_valid():
            pedido_fecha = miForm.cleaned_data.get("fecha")
            pedido_cliente = miForm.cleaned_data.get("cliente")
            pedido_productos =  miForm.cleaned_data.get("productos")
            pedido_cantidad = miForm.cleaned_data.get("cantidad")
            pedido_ubicacion = miForm.cleaned_data.get("ubicacion")
            pedido_estado = miForm.cleaned_data.get("estado")
            pedido = Pedido(fecha = pedido_fecha, cliente = pedido_cliente, productos = pedido_productos,cantidad = pedido_cantidad, ubicacion = pedido_ubicacion, estado = pedido_estado)
            pedido.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Pedido agregado con éxito")
            return redirect(reverse_lazy('pedidos'))
    else:
        miForm = PedidoForm()
        return render(request,"aplicacion/pedidos.html",{"form": miForm}) 
#----------------------------------------------------------READ---------------------------------------------------------------------
@login_required
def pedidos(request):
    formulario_pedido = PedidoForm()
    contexto = {
        'pedidos': Pedido.objects.all(),
        'form': formulario_pedido
    }
    return render(request,"aplicacion/pedidos.html",contexto)
#----------------------------------------------------------UPDATE----------------------------------------------------------------------
@login_required
def pedidoUpdate(request,id_pedido):
    pedido = Pedido.objects.get(id = id_pedido)
    if request.method == "POST":
        miForm = PedidoForm(request.POST)
        if miForm.is_valid():
            pedido.fecha = miForm.cleaned_data.get("fecha")
            pedido.cliente = miForm.cleaned_data.get("cliente")
            pedido.productos =  miForm.cleaned_data.get("productos")
            pedido.cantidad = miForm.cleaned_data.get("cantidad")
            pedido.ubicacion = miForm.cleaned_data.get("ubicacion")
            pedido.estado = miForm.cleaned_data.get("estado")
            
            pedido.save()
            
            return redirect(reverse_lazy('pedidos'))
    else:
        miForm = PedidoForm(initial={'fecha': pedido.fecha, 'cliente' : pedido.cliente, 'productos' : pedido.productos ,'cantidad' : pedido.cantidad, 'ubicacion' : pedido.ubicacion , 'estado': pedido.estado} )
    return render(request,"aplicacion/pedidoForm.html",{"form": miForm})
#----------------------------------------------------------DELETE----------------------------------------------------------------------
@login_required
def pedidoDelete(request,id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    if request.method == 'POST':
        if 'confirmar' in request.POST:
            pedido.delete()
            messages.success(request, f"El pedido '{id_pedido}' ha sido eliminado exitosamente.")
        return redirect('pedidos')
    return render(request, 'aplicacion/pedido_delete.html', {'pedido': pedido})
#endregion
#-------------------------------------------------------BUSCAR-------------------------------------------------------------------------
#region BUSQUEDA
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

@login_required
def buscarPedidos(request):
    return render(request,"aplicacion/buscar.html")

@login_required
def encontrarPedidos(request):
    patron = request.GET.get("buscar")
    if patron:
        pedidos = Pedido.objects.filter(            
            Q(id__icontains=patron) |
            Q(fecha__icontains=patron) |
            Q(cliente__icontains=patron) |
            Q(productos__icontains=patron) |
            Q(cantidad__icontains=patron) |
            Q(ubicacion__icontains=patron) |
            Q(estado__icontains=patron)
)
    else:
        pedidos = Pedido.objects.all()
    
    contexto = {"pedidos": pedidos}
    return render(request, "aplicacion/pedidos.html", contexto)
#endregion
#------------------------------------------LOGIN, LOGOUT, AUTHENTICATION, REGISTRATION-------------------------------------------------------
#region LOGIN y REGISTRO
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
        miForm = CustomAuthenticationForm()
    
    return render(request,"aplicacion/login.html",{"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = CustomUserCreationForm(request.POST)
        
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = CustomUserCreationForm()
    
    return render(request,"aplicacion/registro.html",{"form": miForm})
#endregion
#------------------------------------------EDICIÓN DE PERFIL, CAMBIO DE CLAVE,AVATAR-------------------------------------
#region EDICION DE PERFIL Y AVATAR
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


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
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
#endregion


#----------------------------------------------------COMUNICACION CON EL CLIENTE--------------------------------------------------
# region VERIFICAR DNI DUPLICADO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente  # Asegúrate de importar tu modelo adecuado

@csrf_exempt
def verificar_dni(request):
    if request.method == 'GET':
        dni = request.GET.get('dni', '').strip()  # Obtén el DNI de los parámetros GET y elimina espacios
        if dni:
            # Verifica si el DNI ya existe en la base de datos
            existe = Cliente.objects.filter(dni=dni).exists()
            # Devuelve una respuesta JSON con el resultado
            return JsonResponse({'exists': existe})
        else:
            # Devuelve un error si el DNI no se proporciona
            return JsonResponse({'error': 'DNI no proporcionado'}, status=400)
    else:
        # Devuelve un error si el método no es GET
        return JsonResponse({'error': 'Método no permitido'}, status=405)
#endregion