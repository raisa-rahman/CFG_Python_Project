#Exercise 4.7: Write a program to create a random name. You should have a list of random
# firstnames and a list of lastnames. Choose a random item from each and display the result.

import random

firstname = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ian', 'Jessica']
lastname = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson']

chosen_name = random.choice(firstname) + ' ' + random.choice(lastname)
print(chosen_name)



# Extension: Using list of verbs and a list of nouns, create randomised sentences

verbs = ['jumped', 'ran', 'swam', 'flew', 'danced']
nouns = ['dog', 'cat', 'bird', 'fish', 'rabbit']

sentence = random.choice(nouns) + ' ' + random.choice(verbs)
print('The ' + sentence)