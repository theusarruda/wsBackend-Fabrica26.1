from django.shortcuts import render, redirect
from .services import buscar_pokemon
from .models import Pokemon
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PokemonSerializer

def buscar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data = buscar_pokemon(nome)

        return render(request, 'api_rest/buscar.html', {'pokemon': data})

    return render(request, 'api_rest/buscar.html')

def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data = buscar_pokemon(nome)

        if data:
            Pokemon.objects.create(**data)

        return redirect('listar')

    return render(request, 'api_rest/salvar.html')

def listar(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'api_rest/listar.html', {'pokemons': pokemons})

def deletar(request, id):
    Pokemon.objects.get(id=id).delete()



@api_view(["GET", "POST"])
def pokemon_list_create(request):

    if request.method == "GET":
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        nome = request.data.get("nome")

        data = buscar_pokemon(nome)

        if not data:
            return Response(
                {"erro": "Pokemon não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PokemonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PUT"])
def atualizar_pokemon(request, id):
    try:
        pokemon = Pokemon.objects.get(id=id)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PokemonSerializer(pokemon, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
