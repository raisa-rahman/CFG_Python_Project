#Exercise 3.7: This program simulates rock, paper, scissors. The rst winning condition has been
#added.
#To nish the program you'll need to add all of the other winning and losing conditions.

import random
def random_choice():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
       choice = 'paper'
    return choice
my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()
print('Your opponent chose {}'.format(opponent_choice))
if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')