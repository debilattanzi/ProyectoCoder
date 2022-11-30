from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path('cliente/', cliente, name="cliente"),
    path('proveedor/', proveedor, name="proveedor"),
    path('prendas/', prendas, name="prendas "),

]