import requests
import random

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def library_home_view(request):
    tab = "Biblioteca"
    mensaje = "Bienvenidos a la biblioteca"
    contexto = {"tab": tab,
                "mensaje": mensaje}
    return render(request, 'biblioteca/inicio_template.html', contexto)
