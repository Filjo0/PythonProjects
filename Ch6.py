"""
Chapter 6.
9. Write a program that computes and prints the average of the numbers in a text
file. You should make use of two higher-order functions to simplify the design.
"""


def count_average(file_name):
    with open(file_name) as fh:
        file = fh.read()
    # put numbers into a list
    numbers = [int(word) for word in file.split() if word.isdigit()]

    num_sum = 0

    for index in range(len(numbers)):
        num_sum += numbers[index]

    # get average
    average = (num_sum / len(numbers))

    return print("Average of the numbers in " + "\"" + fh.name + "\" file =", average)


def main():
    print("Hello. This program allows you to get the average of the numbers in a text file.")

    # open your file
    file_name = input("Enter the file name: ")
    count_average(file_name)


main()
