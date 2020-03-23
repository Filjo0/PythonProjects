"""
Chapter 3.
11. In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7,
the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible,
a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so
on. A little mathematical analysis reveals that there are not enough ways to win
to make the game worthwhile; however, because many people’s eyes glaze over
at the first mention of mathematics, your challenge is to write a program that
demonstrates the futility of playing the game. Your program should take as input
the amount of money that the player wants to put into the pot, and play the game
until the pot is e mpty. At that point, the program should print the number of
rolls it took to break the player, as well as maximum amount of money in the pot.
"""

import random
from time import sleep

pot = 0

print("Hello. Lets play \"The Lucky Sevens game\"!",
      "\nRules: You roll a pair of dice. If the dots add up to 7, you WIN $4"
      "\nOtherwise, you lose $1"
      "\nThere are lots of ways to WIN: (1, 6), (2, 5), (3, 4)")
while True:
    try:
        pot = int(input("How much money would you like to deposit into the pot: $"))
        print("Press ENTER to roll a pair of dice")
        input()
    except ValueError:
        print("Please print the number: ")
    while pot > 0:
        print("Rolling...")
        sleep(2)
        dice_roll = random.randint(1, 6), random.randint(1, 6)
        print("You rolled number:", dice_roll[0], "and", dice_roll[1])
        my_roll = (dice_roll[0] + dice_roll[1])
        if my_roll == 7:
            pot += 4
            print("Congratulations! The dots add up to 7! You've won $4 "
                  "\nYour balance is: $" + str(pot),
                  "\nPress ENTER to try again")
        else:
            pot -= 1
            print("Unlucky! The dots add up to:", my_roll, "You've lost $1"
                                                           "\nYour balance is: $" + str(pot),
                  "\nPress ENTER to try again")
        input()
    print("You need to deposit money into your pot")
