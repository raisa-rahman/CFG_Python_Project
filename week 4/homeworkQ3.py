'''
Question 3
Write a program that simulates a lottery. The program should have a list of seven numbers that represent a
lottery ticket. It should then generate seven random numbers. After comparing the two sets of numbers, the
program should output a prize based on the number of matches:

● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers

'''


import random

# Define the lottery ticket
lottery_ticket = [random.randint(1, 50) for _ in range(7)]

# Generate seven random numbers
random_numbers = [random.randint(1, 50) for _ in range(7)]

# Count the number of matching numbers
matches = sum(1 for number in random_numbers if number in lottery_ticket)

# Determine the prize based on the number of matches
prize = None
if matches == 3:
    prize = 20
elif matches == 4:
    prize = 40
elif matches == 5:
    prize = 100
elif matches == 6:
    prize = 10000
elif matches == 7:
    prize = 1000000

# Output the results
print("Lottery ticket numbers:", lottery_ticket)
print("Random numbers drawn:", random_numbers)
print("Number of matching numbers:", matches)
if prize:
    print("Congratulations! You win £{}!".format(prize))
else:
    print("Sorry, you didn't win anything this time.")
