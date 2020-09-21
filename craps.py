"""
Modified code from 'Intro to Python for Computer Science and Data Science',
Authors: Deitel, Paul and Deitel, Harvey,
Published February 25, 2019,
Originally written for Python version 3.7.
"""
​
"""Simulating the dice game Craps."""
import random
from time import sleep
​
def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)  # pack die face values into a tuple
​
def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')
    sleep(1)
​
def display_result(status):
    """Display the outcome of a game."""
    if status == 'WON':
        print('Player wins!')
    else:
        print('Player loses!')
​
def play_craps():
    """Start a game of craps."""
    die_values = roll_dice()  # first roll
    display_dice(die_values)
​
    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)
    num_rolls = 1
​
    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        print('Point is', my_point)
​
    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)
​
        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
            
        num_rolls += 1
​
    print(f'Number of rolls: {num_rolls}')
​
    # display "wins" or "loses" message
    display_result(game_status)
​
play_craps()