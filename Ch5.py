"""
Chapter 5.
2. Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number.
"""

print("Hello. This program allows you to navigate through the lines of text in a file")

fileName = input("Enter the file name: ")

with open(fileName) as fh:
    lines = fh.readlines()
    fh.close()
    print("The number of lines in the " + "\"" + fh.name + "\" file is", len(lines))

while True:
    num = int(input("Please enter a line number or press 0 to quit: "))

    if 0 < num < len(lines) + 1:
        print(lines[num - 1])

    elif num >= len(lines) + 1:
        print("This line number is too big!"
              "\nThe number of lines in the " + "\"" + fh.name + "\" file is", len(lines))

    elif num == 0:
        print("Thanks for using the program")
        break
