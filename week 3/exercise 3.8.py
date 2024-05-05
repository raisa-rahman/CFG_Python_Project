#Exercise 3.8: Not Quite Roulette
#Ask the user to enter the following three things using input() :

#The amount they want to bet
#A colour (red or black)
#A number between 1 and 100
#After generating a random number and colour:

# If the colour matches, the users keeps the amount that was bet
    # If the number matches, the users wins double the amount that was bet
    # If the colour and number matches, the users wins 100 times the amount that was bet
    # When neither the colour or number matches the user wins 0
    # Output the amount the user won

import random
def random_number():
    random_number = random.randint(1, 100)
    return random_number

def random_colour():
    random_colour = random.randint(1, 2)
    if random_colour != 1:
        colour = 'red'
    else:
        colour = 'black'
    return colour


amount = input('How much would you like to bet? ')
colour = input('Choose a colour: red or black ')
number = input('Pick a number between 1 and 100: ')

opponent_colour = colour()
opponent_number = number()

number_win_amount = amount * 2
number_and_colour_win_amount = amount * 100

if colour == random_colour():
    print('The colour your opponent chose {} so you get to keep {}'.format(colour, amount))

if number == random_number():
    print('The number your opponent chose {} so you earn {}'.format(random_number(), number_win_amount))

if number == random_number() and colour == random_colour():
    print('The number your opponent chose {}, the colour your opponent chose {} so you earn {}'.format(random_number(), random_colour(), number_and_colour_win_amount))

if number != random_number() and colour != random_colour():
    print('The number your opponent chose {}, the colour your opponent chose {} so you earn 0'.format(random_number(), random_colour()))