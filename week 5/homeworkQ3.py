'''
In this session you used the Pokemon API to retrieve a single Pokemon.
I want a program that can retrieve multiple Pokemon and save their names and moves to a file.
Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
Pokemon. Save their names and moves into a file called 'pokemon.txt'
'''

import requests

pokemon_ids = [1,2,3,4,5,6,7]  # Example IDs: Bulbasaur, Charmander, Squirtle, Pikachu, Jigglypuff, Eevee

def get_pokemon_data(id):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    response = requests.get(url)
    if response.status_code == 200:
        pokemon = response.json()
        name = pokemon['name']
        moves = pokemon ['moves']
        moves_string = ''
        for move in moves:
            moves_string += move ['move']['name']
        return f'Pokemon {name} had {moves_string}'
    else:
        print(f"Error!{id} not a valid id")

for id in pokemon_ids:
    pokemon_data = get_pokemon_data(id)
    if pokemon_data:
        with open('pokemon.txt', 'a') as pokemon_file:
            pokemon_file.write(pokemon_data + '\n')
            print(f"Information of pokemon {id} was written to the file")
