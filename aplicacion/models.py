from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.IntegerField()
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio  = models.FloatField()
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    color = models.CharField(max_length=50) 
    talla = models.CharField(max_length=50) 
    
    
    def __str__(self):
        return f"{self.nombre}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.IntegerField(unique=True)
    sueldo = models.FloatField()
    def __str__(self):
        return f"{self.nombre},{self.apellido}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"

class Pedido(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.IntegerField()
    productos = models.CharField(max_length=255) 
    cantidad = models.IntegerField()  
    ubicacion = models.CharField(max_length=100) 
    estado = models.CharField(max_length=50)  

    def __str__(self):
        return self.fecha.strftime('%d/%m/%Y')
