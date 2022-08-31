#from dataclasses import field
#from pyexpat import model
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        #fields = ["nombre", "apellido", "nombre_de_usuario", "correo", "contraseña"]
        fields = "__all__"

class Registro(UserCreationForm):
    pass
    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "username", "correo"]