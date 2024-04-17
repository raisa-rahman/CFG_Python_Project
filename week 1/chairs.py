# I am building some very high quality chairs and need exactly four nails for each chair. I've written a
# program to calculate how many nails I need to buy to build these chairs.
# chairs = '15'
# nails = 4
# total_nails = chairs * nails
# message = 'I need to buy {} nails'.format(total_nails)
# print('You need to buy {} nails'.format(message))
# When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails. Is
# my program calculating the total number of nails correctly? What is the problem? How do I fix it?

chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))

# the program was not calculating the correct number of nails
# the problem is that 15 was written as a string and not an integer - to fix it I removed ''
