# Enter you module contents here

"Includes functions to calculate the hypotenuse and the area of a right triangle."

__author__ = "Aleks Hiidenhovi"
__version__ = "1.0"

from math import sqrt

def hypothenuse(a, b):
    "Calculate the hypotenuse of a right triangle with sides a and b."
    return sqrt(a**2 + b**2)

def area(a, b):
    "Calculate the area of a right triangle with perpendicular sides a and b."
    return a * b / 2