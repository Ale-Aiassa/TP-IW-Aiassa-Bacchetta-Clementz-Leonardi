from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def SecondPage(request):
    return render(request, "SecondPage.html")
