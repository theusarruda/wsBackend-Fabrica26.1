from django.urls import path
from . import views
from .views import pokemon_list_create, atualizar_pokemon

urlpatterns = [
    path('buscar/<str:nome>/', views.buscar),
    path('', views.listar, name='listar'),
    path('salvar/', views.salvar, name='salvar'),
    path('deletar/<int:id>/', views.deletar),
    path('pokemons/', pokemon_list_create),
    path('pokemons/<int:id>/', atualizar_pokemon),
]
