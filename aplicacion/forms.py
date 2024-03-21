from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirma tu contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50,required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50,required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirma tu contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)