from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home,name="home"),
    path('about/', clientes,name="about"),
    path('store/', empleados,name="store"),
    path('products/', productos,name="products"),
    #--------------Formularios
    path('clienteForm/', clienteForm, name="cliente_form"),
]
