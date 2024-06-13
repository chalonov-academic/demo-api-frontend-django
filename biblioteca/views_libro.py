import requests
import random

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import IsbnForm


url_api = 'http://localhost:9090/biblioteca/libro'


def api_request(url):
    return requests.get(url).json()


def users_list(request):
    contexto = api_request(url_api)
    template = loader.get_template('libros/list_template.html')
    return HttpResponse(template.render({'users': contexto}, request))


def user_search(request):
    form = IsbnForm(request.POST or None)
    information = ''
    url = url_api

    if form.is_valid():
        numero = form.cleaned_data['numeroIsbn']
        url += f'/{numero}'

        try:
            # Realizar la solicitud a la API con el número ingresado
            response = requests.get(url)
            response.raise_for_status()

            # lógica para manejar la respuesta de la API
            information = response.text
        except requests.exceptions.RequestException as e:
            information = f'Error al realizar la solicitud a la API: {e}'

    contexto = {
        'form': form,
        'information': information,
        'users': requests.get(url).json(),
    }

    return render(request, 'libros/search_template.html', contexto)