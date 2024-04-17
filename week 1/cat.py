#Exercise 1.4: In a new Python le called cat_food.py , create a program that calculates how many cans of cat food you need to feed 10 cats

cats = 10
can = 2
total_cans = cats * can
output = str(cats) + " cats eat " +str(total_cans) + " cans "
print (output)

#Extension: change the calculation to work out the amount needed for 7 days

days = 7
total_cans = cats * can * days

output = str(cats) + " cats eat " + str (total_cans) + " cans in " + str(days) + " days."
print(output)

#Exercise 1.5: Rewrite cat_food.py to use string formatting instead of joining strings with +

output = '{} cats eat {} cans in {} days.'.format(cats, total_cans, days)
print (output)