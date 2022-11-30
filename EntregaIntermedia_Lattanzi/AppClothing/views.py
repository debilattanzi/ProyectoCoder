from django.shortcuts import render
from AppClothing.models import *

# Create your views here.

def inicio(request):
    return render(request, "AppClothing/inicio.html")


def cliente(request):
    return render(request, "AppClothing/cliente.html")


def proveedor(request):
    return render(request, "AppClothing/proveedor.html")

def prendas(request):
    return render(request, "AppClothing/prendas.html")
