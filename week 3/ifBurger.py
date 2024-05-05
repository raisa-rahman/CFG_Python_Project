#Exercise 3.3: Rewrite the output of your burger program to use if statements
#If it is a good choice it should be:
#This restaurant is a great choice!

#If it is not a good choice it should be:
#Probably not a good idea

price = input("What is the price of the burger? ")
budgetPrice = float(price) <= 10

option = input("Is there a vegetarion option? (y/n) ")
veg = (option) == 'y'

print ("Burger is within budget: {}".format(budgetPrice))
print ("Restaurant meets criteria: {}".format(veg))

good_choice = budgetPrice and veg
if good_choice:
    print('This restaurant is a great choice!')
if not good_choice:
    print('Probably not a good idea')

