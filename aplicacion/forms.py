from django import forms
from .models import Pedido
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    dni = forms.IntegerField(required=True)
    apellido = forms.CharField(max_length=50,required=True)
    edad = forms.IntegerField(required=True)

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if not isinstance(dni, int) or len(str(dni)) != 8:
            raise forms.ValidationError('El DNI debe ser un número de 8 dígitos.')
        return dni

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
    password2 = forms.CharField(label="Confirma tu contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50,required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50,required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)


class PedidoForm(forms.Form):
    fecha = forms.DateTimeField(required=True)
    cliente = forms.IntegerField(required=True)
    productos = forms.CharField(max_length=255,required=True) 
    cantidad = forms.IntegerField(required=True)  
    ubicacion = forms.CharField(max_length=100,required=True) 
    estado = forms.CharField(max_length=50,required=True)
    
    class Meta:
        fields = ['cliente', 'productos', 'cantidad', 'ubicacion', 'estado']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'readonly': 'readonly'}),  
            }
        
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Usuario"

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma tu contraseña", widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Usuario"
