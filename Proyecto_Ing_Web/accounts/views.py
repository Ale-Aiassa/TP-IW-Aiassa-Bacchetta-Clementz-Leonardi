from email import message
from tkinter.messagebox import Message
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Usuario
from .forms import Registro
from django.contrib.auth import authenticate, login

def home2(request):
    return render(request, 'home2.html')

def home(request):
    return render(request, 'home.html')

def SecondPage(request):
    return render(request, 'SecondPage.html')

def login(request):
    return render(request, 'registration/login.html')


def signup(request):
    data = {
        "form": Registro()
    }
    if request.method == "POST":
        formulario = Registro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            Usuario = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password"])
            login(request, Usuario)
            #Message.success(request, "Registro exitoso")
            #redirigir al home
            return redirect(to="SecondPage")
        data["form"] = formulario
    return render(request, 'registration/signup.html', data)


#class SignUpView(generic.CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy("login")
#    template_name = "registration/signup.html"
