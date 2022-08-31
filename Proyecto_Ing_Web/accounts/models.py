from pickle import TRUE
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20, unique=True, blank=False, null=False, default="Nombre obligatorio")
    apellido = models.CharField(max_length=30, blank=False, null=False, default="Apellido obligatorio")
    username = models.CharField(max_length=30, blank=False, null=False, default="Username obligatorio")
    correo = models.EmailField(max_length=254, unique=True, null=False, blank=False, default="Correo Obligatorio")
    password = models.CharField(max_length=40, unique=True, null= False, blank=False, default="Password obligatorio")
    USERNAME_FIELD = 'correo'
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre