"""
Chapter 1.
6. Write and test a program that computes the area of a circle. This program should
request a number representing a radius as input from the user. It should use the formula
3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
"""
from math import pi


def area_of_circle():
    area = float(int(input("Please print the radius of the circle: ")))
    print("The area of the circle with radius " + str(area) + " is: " + str(pi * area ** 2))


area_of_circle()
