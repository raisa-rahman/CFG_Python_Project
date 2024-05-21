'''Question 2

I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different
chocolates that I sell. I've started the program and included the chocolates and their prices. Finish the
program by asking the user to input an item and then output its price.

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

'''

chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

chocolate_type = input("Which chocolate would you like to buy? (white/milk/dark/vegan) ")

# Check if the chocolate type exists in the dictionary
if chocolate_type in chocolates:
    # If it exists, print its price
    print(f"The price of {chocolate_type} chocolate is ${chocolates[chocolate_type]:.2f}")
else:
    # If it doesn't exist, inform the user
    print("Sorry, we don't have that type of chocolate.")