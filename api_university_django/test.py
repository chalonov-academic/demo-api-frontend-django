import requests


def autor_lista():
    endpoint = 'http://localhost:9090/biblioteca/autor'
    api_request = f"{endpoint}"
    response = requests.get(api_request)
    autores = response.json()
    return autores


autor_a_mostrar = autor_lista()
print(autor_a_mostrar)
