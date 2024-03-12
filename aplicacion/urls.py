from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home,name="home"),
    path('about/', about,name="about"),
    path('store/', store,name="store"),
    path('productos/', productos,name="productos"),
    path('clientes/', clientes,name="clientes"),
    path('empleados/', empleados,name="empleados"),
    #---------------------------------------------------Formularios
    path('clienteForm/', clienteForm, name="cliente_form"),
    path('empleadoForm/', empleadoForm, name="empleado_form"),
    path('productoForm/', productoForm, name="producto_form"),
    
    #LOGIN
    # path('login/', login,name="login"),
    #----------------------------------------------------Busqueda
    path('buscar_clientes/', buscarClientes, name="buscar_clientes"),
    path('encontrar_clientes/', encontrarClientes, name="encontrar_clientes"),
    path('buscar_empleados/', buscarEmpleados, name="buscar_empleados"),
    path('encontrar_empleados/', encontrarEmpleados, name="encontrar_empleados"),
    path('buscar_productos/', buscarProductos, name="buscar_productos"),
    path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),
]
