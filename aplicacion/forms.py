from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    dni = forms.IntegerField(required=True)
    apellido = forms.CharField(max_length=50,required=True)
    edad = forms.IntegerField(required=True)

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    dni = forms.IntegerField(required=True)
    apellido = forms.CharField(max_length=50,required=True)
    edad = forms.IntegerField(required=True)
    sueldo = forms.FloatField(required=True)
    
class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    precio = forms.FloatField(required=True)
    marca = forms.CharField(max_length=50,required=True)
    stock = forms.IntegerField(required=True)
    color = forms.CharField(max_length=50,required=True)
    talla = forms.CharField(max_length=50,required=True)

# class LoginForm(forms.Form):
#     usuario = forms.CharField(max_length=50,required=True)
#     contraseña = forms.CharField(max_length=50,required=True)