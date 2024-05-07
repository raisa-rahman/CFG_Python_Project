#Exercise 3.2: Add code to your burger program to input whether the restaurant has a vegetarian
#option The output should say whether the cost is within budget AND has a vegetarian option
#Restaurant meets criteria: True
from tokenize import String

price = input("What is the price of the burger? ")
option = input("Is there a vegetarion option? (y/n) ")
budgetPrice = float(price) <= 10
veg = (option) == 'y'

print ("Burger is within budget: {}".format(budgetPrice))
print ("Restaurant meets criteria: {}".format(veg))