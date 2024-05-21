#Exercise 4.2: Make a list of game scores. Using list functions write code to output
# information of the scores in the following format:

#Number of scores: 10
#Highest score: 200
#Lowest score: 3

game_scores = [
    200, 3, 100, 150, 175, 25, 50, 75, 100, 125
]

print('Number of scores: ' + str(len(game_scores)))
print('Highest score: ' + str(max(game_scores)))
print('Lowest score: ' + str(min(game_scores)))

#Extension: Output all of the scores in descending order

sorted_scores = sorted(game_scores, reverse=True)
print('All scores in descending order:', sorted_scores)