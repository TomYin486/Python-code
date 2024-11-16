"""
Game rules:
1. Two players (Player1 and Player2) take turns rolling the dice.
2. Each roll results in a score, which can be positive (the sum of two dice) or negative (if both dice show 1, the score is -1).
3. The player's score is updated based on the roll. If the roll results in a negative score, the player's score is reset to 0.
4. The game continues until one player's score reaches or exceeds 100 points.
5. At the end of the game, the winner is announced. If both players have the same score, a tie is declared.
"""

# Import Python's random module for generating random numbers (used to simulate dice rolling)
import random

# Check if the game is over
# If either player's score reaches or exceeds 100 points, the function returns True, indicating the game is over
def gameover(score1, score2):
    over = False
    if score1 >= 100 or score2 >= 100:
        over = True
    return over

# Simulate rolling two dice
# If both dice show 1, the player loses the current round's score (point = -1); otherwise, the player's score is the sum of the two dice
def castDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    point = 0
    if die1 == 1 and die2 == 1:
        point = -1
    elif die1 != 1 and die2 != 1:
        point = die1 + die2
    return point

# Update the player's score
# If the player's round score is not negative (i.e., did not roll two 1s), add it to the total score; if it is negative, reset the total score to 0
def updateScore(point, score):
    if point != -1:
        score += point
    else:
        score = 0
    return score

# Announce the winner at the end of the game
# If Player1's score is higher than Player2's, announce Player1 as the winner; vice versa; if the scores are the same, declare a tie
def displayWinner(s1, s2):
    if s1 > s2:
        print('The winner is Player1')
    elif s1 < s2:
        print('The winner is Player2')
    else:
        print('Both players have the same score')

score1 = 0
score2 = 0

while not gameover(score1, score2):
    # Player1 rolls the dice, updates the score, and prints Player1's round score and total score
    point = castDice()
    score1 = updateScore(point, score1)
    print('Player1', point, score1)

    # Player2 rolls the dice, updates the score, and prints Player2's round score and total score
    point = castDice()
    score2 = updateScore(point, score2)
    print('Player2', point, score2)
    print('-------------------------------')

displayWinner(score1, score2)

