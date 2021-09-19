#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    square_root = math.sqrt(b**2 - 4*a*c)
    
    ans1 = (-b + square_root) / (2*a)
    ans2 = (-b - square_root) / (2*a)
    
    return (ans1, ans2)
    


def main():
    print(solve_quadratic(1, 3, 2))

if __name__ == "__main__":
    main()
