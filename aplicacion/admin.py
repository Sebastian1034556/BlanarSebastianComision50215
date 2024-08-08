from django.contrib import admin

# Register your models here.

from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido")

class LoginAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)
admin.site.register(UserProfile)
