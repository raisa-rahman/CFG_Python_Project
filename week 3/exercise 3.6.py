#Exercise 3.6: This program uses random to simulate a coin ip.
#To nish the program you will need to add the following:

#If the random coin ip matches the choice input by the user then they win
#Ohterwise if the random coin ip does not match the choice input by the user then they lose

import random
def flip_coin():
    random_number = random.randint(1, 2)
    if random_number != 1:
        side = 'tails'
    else:
        side = 'heads'
    return side
choice = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))