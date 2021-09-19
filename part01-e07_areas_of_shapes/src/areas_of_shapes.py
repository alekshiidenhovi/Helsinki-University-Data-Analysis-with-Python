#!/usr/bin/env python3

import math


def main():
    exit = False
    while not exit: 
        choose = input("Choose a shape (triangle, rectangle, circle): ")
        if choose == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            print(f"The area is {base * height / 2}")
        elif choose == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            print(f"The area is {width * height}")
        elif choose == "circle":
            radius = float(input("Give radius of the circle: "))
            print(f"The area is {math.pi * radius**2}")
        elif choose == "":
            exit = True
        else:
            print(f"Unknown shape!")

if __name__ == "__main__":
    main()
