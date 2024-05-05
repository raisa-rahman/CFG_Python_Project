#Exercise 3.1: You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

#1. Input the price of a burger using input()
#2. Check whether the price is less than or equal (<=) 10.00
#3. Print the result in the format below
#Burger is within budget: True

#Hint: remember to convert the input from a string to a decimal with float()

price = input("What is the price of the burger? ")
budgetPrice = float(price) <= 10

print ("Burger is within budget: {}".format(budgetPrice))