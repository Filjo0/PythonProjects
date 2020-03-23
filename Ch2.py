"""
Chapter 2.
3. Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
like to buy LP record albums. The store rents new videos for $3.00 a night, and
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals. The program
should prompt the user for the number of each type of video and output the total
cost.
"""
from time import sleep


def count_full_price():
    new_price = 3
    old_price = 2
    new = int(input("Hello. Please print how many new videos ($3.00 a night) are you going to rent?"))
    new_nights = int(input("Please print for how many nights are you going to rent the new ones?"))
    old = int(input("Please print how many old videos ($2.00 a night) are you going to rent?"))
    old_nights = int(input("Please print for how many nights are you going to rent the old ones?"))
    full_price = (new * new_price * new_nights) + (old * old_price * old_nights)
    print(
        "You are going to rent: " + str(new) + " new video(s) for " + str(new_nights) + " night(s) and " +
        str(old) + " old video(s) for " + str(old_nights) + " night(s).")
    sleep(2)
    print("It will cost you: $" + str(float(full_price)))


count_full_price()
