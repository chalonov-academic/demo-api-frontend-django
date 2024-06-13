import requests
import random

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import IdForm


url_api = 'https://university-full.azurewebsites.net/biblioteca/autor'


def api_request(url):
    return requests.get(url).json()


def users_list(request):
    contexto = api_request(url_api)
    template = loader.get_template('autores/list_template.html')
    return HttpResponse(template.render({'users': contexto}, request))


def user_random(request):
    data = api_request(url_api)
    indice_random = random.randrange(1, len(data) + 1)
    api_request_random = f"{url_api}/{indice_random}"
    contexto = requests.get(api_request_random).json()
    template = loader.get_template('autores/random_template.html')
    return HttpResponse(template.render({'users': contexto}, request))


def user_search(request):
    form = IdForm(request.POST or None)
    information = ''
    url = url_api

    if form.is_valid():
        numero = form.cleaned_data['numeroId']
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

    return render(request, 'autores/search_template.html', contexto)