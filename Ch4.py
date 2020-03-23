"""
Chapter 4.
10. Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines is found.
"""

# Open the input files
from itertools import zip_longest

# Take the inputs
fileName1 = input("Enter the first file name: ")
fileName2 = input("Enter the second file name: ")


def count_line():
    line_count = 1
    # Read each pair of lines and compare them
    with open(fileName1) as fh1, open(fileName2) as fh2:
        for line1, line2 in zip_longest(fh1, fh2):
            # line1 from fileName1, line2 from fileName2

            if line1 == line2:
                if line_count == len(line1) + 1:
                    print("Yes")
                    break

            elif line1 != line2:
                print("No")
                print("Line №", line_count, "of file \"" + fh1.name + "\" with text:", line1,
                      "\ndiffers from the line of file \"" + fh2.name + "\" with text:", line2)
                break
            line_count += 1


count_line()
