from django.shortcuts import render
from AppFamily.models import Familia
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def familiares(request):
    familiar1 = Familia(nombre="Damian", apellido="Mangold", fechaNacimiento="1987-02-05", edad=35, parentesco="Marido")
    familiar2 = Familia(nombre="Felipe", apellido="Aimonetto Lattanzi", fechaNacimiento="2010-09-29", edad=12,
                        parentesco="Hijo")
    familiar3 = Familia(nombre="Valentina", apellido="Mangold Lattanzi", fechaNacimiento="2021-04-21", edad=1,
                        parentesco="Hija")

    diccionario = {"familiar1Nombre": familiar1.nombre, "familiar1Apellido": familiar1.apellido,
                   "familiar1Nacimiento": familiar1.fechaNacimiento, "familiar1Edad": familiar1.edad,
                   "familiar1Parentesco": familiar1.parentesco,
                   "familiar2Nombre": familiar2.nombre, "familiar2Apellido": familiar2.apellido,
                   "familiar2Nacimiento": familiar2.fechaNacimiento, "familiar2Edad": familiar2.edad,
                   "familiar2Parentesco": familiar2.parentesco,
                   "familiar3Nombre": familiar3.nombre, "familiar3Apellido": familiar3.apellido,
                   "familiar3Nacimiento": familiar3.fechaNacimiento, "familiar3Edad": familiar3.edad,
                   "familiar3Parentesco": familiar3.parentesco}

    familiar1.save()
    familiar2.save()
    familiar3.save()

    plantilla = loader.get_template("templateFamily.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
