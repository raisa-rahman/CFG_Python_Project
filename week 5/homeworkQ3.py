'''
In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can
retrieve multiple Pokemon and save their names and moves to a file.
Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
Pokemon. Save their names and moves into a file called 'pokemon.txt'
'''

import requests

# List of Pokémon IDs
pokemon_ids = [1, 4, 7, 25, 39, 133]  # Example IDs: Bulbasaur, Charmander, Squirtle, Pikachu, Jigglypuff, Eevee

# URL template for the Pokémon API
url_template = "https://pokeapi.co/api/v2/pokemon/{}"

# File to save Pokémon names and moves
output_file = "pokemon.txt"

# Function to get Pokémon data
def get_pokemon_data(pokemon_id):
    url = url_template.format(pokemon_id)
    response = requests.get(url)
    return response.json()

# Function to save Pokémon names and moves to a file
def save_pokemon_data(pokemon_list, file_name):
    with open(file_name, 'w') as file:
        for pokemon in pokemon_list:
            file.write(f"Name: {pokemon['name']}\n")
            file.write("Moves:\n")
            for move in pokemon['moves']:
                file.write(f" - {move['move']['name']}\n")
            file.write("\n")

# Main script
def main():
    pokemon_list = []

    for pokemon_id in pokemon_ids:
        data = get_pokemon_data(pokemon_id)
        pokemon_list.append(data)

    save_pokemon_data(pokemon_list, output_file)
    print(f"Saved Pokémon data to {output_file}")

if __name__ == "__main__":
    main()
