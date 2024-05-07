#Question 1
#Create a program that tells you whether or not you need an umbrella when you leave the house.
#The program should:
#1. Ask you if it is raining using input()
#2. If the input is 'y', it should output 'Take an umbrella'
#3. If the input is 'n', it should output 'You don't need an umbrella'

question = input('Is it raining outside? (y/n) ')

if question == 'y':
    print ('take an umbrella')
else:
    print('you dont need an umbrella')
