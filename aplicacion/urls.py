from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home,name="home"),
    path('about/', about,name="about"),
    path('store/', store,name="store"),
    path('products/', productos,name="products"),
    path('clientes/', clientes,name="clientes"),
    path('empleados/', empleados,name="empleados"),
    #---------------------------------------------------Formularios
    path('clienteForm/', clienteForm, name="cliente_form"),
    path('empleadoForm/', empleadoForm, name="empleado_form"),
    #----------------------------------------------------Busqueda
    path('buscar_clientes/', buscarClientes, name="buscar_clientes"),
    path('encontrar_clientes/', encontrarClientes, name="encontrar_clientes"),
]
