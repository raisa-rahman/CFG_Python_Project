import random
import requests


def random_pokemon():
    """Fetch a random Pokemon's data from the PokeAPI."""
    pokemon_number = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


def run():
    """Main function to run the Top Trumps game."""
    my_pokemon = random_pokemon()
    print(f'You were given {my_pokemon["name"].capitalize()}')

    # Get the player's choice of stat
    stat_choice = input('Which stat do you want to use? (id, height, weight) ').lower()
    while stat_choice not in ['id', 'height', 'weight']:
        stat_choice = input('Invalid choice. Please choose from (id, height, weight): ').lower()

    opponent_pokemon = random_pokemon()
    print(f'The opponent chose {opponent_pokemon["name"].capitalize()}')

    # Compare the chosen stats
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')


# Run the game
run()