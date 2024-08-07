from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from .api import ProductoViewSet,PedidoViewSet


router = routers.DefaultRouter()
router.register('products',ProductoViewSet, 'product')
router.register('orders',PedidoViewSet, 'order')


urlpatterns = [
    path('', home,name="home"),
    path('store/', store,name="store"),
    path('checkout/', checkout,name="checkout"),
    path('productos/', productos,name="productos"),
    path('clientes/', clientes,name="clientes"),
    path('empleados/', empleados,name="empleados"),
    path('pedidos/', pedidos,name="pedidos"),
    #---------------------------------------------------Formularios
    path('clienteCreate/', clienteCreate, name="cliente_create"),
    path('clienteUpdate/<id_cliente>/', clienteUpdate, name="cliente_update"),
    path('cliente_delete/<id_cliente>/', clienteDelete, name='cliente_delete'),
    
    path('empleadoCreate/', empleadoCreate, name="empleado_create"),
    path('empleadoUpdate/<id_empleado>/', empleadoUpdate, name="empleado_update"),
    path('empleado_delete/<id_empleado>/', empleadoDelete, name="empleado_delete"),
    
    path('productoCreate/', productoCreate, name="producto_create"),
    path('productoUpdate/<id_producto>/', productoUpdate, name="producto_update"),
    path('producto_delete/<id_producto>/', productoDelete, name="producto_delete"),
    
    path('pedidoCreate/', pedidoCreate, name="pedido_create"),
    path('pedidoUpdate/<id_pedido>/', pedidoUpdate, name="pedido_update"),
    path('pedido_delete/<id_pedido>/', pedidoDelete, name="pedido_delete"),
    
    #----------------------------------------------------Busqueda
    path('buscar_clientes/', buscarClientes, name="buscar_clientes"),
    path('encontrar_clientes/', encontrarClientes, name="encontrar_clientes"),
    
    path('buscar_empleados/', buscarEmpleados, name="buscar_empleados"),
    path('encontrar_empleados/', encontrarEmpleados, name="encontrar_empleados"),
    
    path('buscar_productos/', buscarProductos, name="buscar_productos"),
    path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),
    
    path('buscar_pedidos/', buscarPedidos, name="buscar_pedidos"),
    path('encontrar_pedidos/', encontrarPedidos, name="encontrar_pedidos"),
    #----------------------------------------------------Login, logout, registration
    path('login/', login_request, name='login'),
    path('logout/',LogoutView.as_view(template_name="aplicacion/logout.html"), name='logout'),
    path('registrar/', register , name='registrar'),
    #----------------------------------------------------Edicion perfil, Cambio de clave, Avatar
    path('perfil/',editProfile, name="perfil"),
    path('<int:pk>/password/',CambiarClave.as_view(), name='cambiar_clave'),        
    path('agregarAvatar/',agregarAvatar, name="agregar_avatar"),
    #----------------------------------------------------Comunicacion con el cliente
    path('verificarDni/', verificar_dni, name='verificar_dni'),
    path('obtener_direccion/', obtener_direccion, name='obtener_direccion'),
    path('api/', include(router.urls)),
]  
