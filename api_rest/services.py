import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return {
            "nome": data["name"],
            "numero": data["id"],
            "tipo": data["types"][0]["type"]["name"],
            "imagem": data["sprites"]["front_default"]
        }

    return None