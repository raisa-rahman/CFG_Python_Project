#Exercise 4.6: Using a for loop, output the values name , colour and price of each dictionary
# in the list

fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruits in fruits:
    print(fruits['name'])
    print(fruits['colour'])
    print(fruits['price'])

