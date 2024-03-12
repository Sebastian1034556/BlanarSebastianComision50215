from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre},{self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio  = models.FloatField(max_length=50)
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
    dni = models.IntegerField()
    sueldo = models.FloatField()
    def __str__(self):
        return f"{self.nombre},{self.apellido}"
    
# class Login(models.Model):
#     usuario = models.CharField(max_length=50)
#     contraseña = models.CharField(max_length=50)
    
#     def __str__(self):
#         return f"{self.usuario},{self.contraseña}"