# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can
# make. Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
# able to easily change these values if I want. The output should say something like "You can make 9
# omelettes with 6 boxes of eggs".

eggs_per_box = 6
eggs_per_omlette = 4
num_boxes = 6
total_eggs = num_boxes * eggs_per_box
omlettes = total_eggs // eggs_per_omlette

output = "You can make {} omelettes with {} boxes of eggs".format(omlettes, num_boxes)
print (output)
