from django.contrib import admin

# Register your models here.

from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido")
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Producto)
admin.site.register(Empleado)
