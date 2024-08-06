import json
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')
django.setup()

# Importar el modelo
from aplicacion.models import Producto

# Leer el archivo JSON
with open('productos.json', 'r') as f:
    productos = json.load(f)

# Insertar los datos en la base de datos
for producto in productos:
    Producto.objects.create(
        nombre=producto['nombre'],
        precio=producto['precio'],
        marca=producto['marca'],
        stock=producto.get('stock', 0),
        color=producto.get('color', 'Desconocido'),
        talla=producto.get('talla', 'Única'),
        imagen=producto['imagen'],
        cantidad=producto['cantidad']
    )
