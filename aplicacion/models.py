from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.IntegerField(unique=True)
    
    def clean(self):
        # Validar que nombre y apellido no contengan nada que no sean letras
        for field_value, field_name in [(self.nombre, 'nombre'), (self.apellido, 'apellido')]:
            for char in field_value:
                if not char.isalpha():
                    raise ValidationError({field_name: f'El {field_name} solo puede contener letras.'})
            
            if len(field_value) < 3:
                raise ValidationError({field_name: f'El {field_name} debe tener al menos 3 caracteres.'})

        if not (18 <= self.edad <= 120):
            raise ValidationError({'edad': 'La edad debe ser de entre 18 y 120 años'})
        
        dni_str = str(self.dni)
        if not (8 <= len(dni_str) <= 10):
            raise ValidationError({'dni': 'El DNI debe tener entre 8 y 10 dígitos.'})


    
    def save(self, *args, **kwargs):
        self.full_clean()  # Esto llama a self.clean() y valida el modelo.
        super(Cliente, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.nombre},{self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio  = models.FloatField()
    marca = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    color = models.CharField(max_length=50) 
    talla = models.CharField(max_length=50) 
    
    def clean(self):
        for field_value, field_name in [(self.nombre, 'nombre'), (self.marca, 'marca'), (self.color, 'color')]:
            if len(field_value) < 3:
                raise ValidationError({field_name: f'El {field_name} debe tener al menos 3 caracteres.'})

        if self.precio <= 0:
            raise ValidationError({'precio': 'El precio debe ser un valor positivo.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Producto, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.nombre}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.IntegerField(unique=True)
    sueldo = models.FloatField()
    
    def clean(self):
        for field_value, field_name in [(self.nombre, 'nombre'), (self.apellido, 'apellido')]:
            for char in field_value:
                if not char.isalpha():
                    raise ValidationError({field_name: f'El {field_name} solo puede contener letras.'})
            
            if len(field_value) < 3:
                raise ValidationError({field_name: f'El {field_name} debe tener al menos 3 caracteres.'})

        if not (18 <= self.edad <= 120):
            raise ValidationError({'edad': 'La edad debe ser de entre 18 y 120 años'})
        
        dni_str = str(self.dni)
        if not (8 <= len(dni_str) <= 10):
            raise ValidationError({'dni': 'El DNI debe tener entre 8 y 10 dígitos.'})
        
        if self.sueldo <= 0:
            raise ValidationError({'sueldo': 'El sueldo debe ser un valor positivo.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Esto llama a self.clean() y valida el modelo.
        super(Empleado, self).save(*args, **kwargs)
            
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
    productos = models.CharField(max_length=50) 
    cantidad = models.IntegerField()  
    ubicacion = models.CharField(max_length=50) 
    estado = models.CharField(max_length=50)  
    
    def clean(self):
        for field_value, field_name in [(self.productos, 'productos'), (self.estado, 'estado')]:
            if len(field_value) < 3:
                raise ValidationError({field_name: f'El {field_name} debe tener al menos 3 caracteres.'})
        
        if self.cliente <= 1000:
            raise ValidationError({'cliente': 'El id del cliente debe ser mayor que 1000.'})
        
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': 'El cantidad debe ser un valor positivo.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Esto llama a self.clean() y valida el modelo.
        super(Pedido, self).save(*args, **kwargs)

    def __str__(self):
        return self.fecha.strftime('%d/%m/%Y')
