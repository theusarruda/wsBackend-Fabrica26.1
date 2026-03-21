from django.shortcuts import render
from .services import buscar_pokemon

def buscar(request):
    pokemon = None

    if 'nome' in request.GET:
        nome = request.GET['nome']
        pokemon = buscar_pokemon(nome)

    return render(request, 'buscar.html', {'pokemon': pokemon})
# Create your views here.
