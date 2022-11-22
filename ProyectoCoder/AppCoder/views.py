from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.
def  curso(request):

    curso=Curso(nombre="Python-Django", comision=12345)
    curso.save()

    cadena_Texto="Curso Guardado: "+curso.nombre+" "+str(curso.comision)

    return HttpResponse(cadena_Texto)