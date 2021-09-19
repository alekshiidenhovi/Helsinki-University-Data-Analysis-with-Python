#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        
    nums = []
    for line in lines:
        try:
            nums.append(float(line))
        except ValueError:
            continue
            
    n = len(nums)
    
    s = sum(nums)
    mean = s / n
    variance = sum([(num - mean)**2 for num in nums]) / (n - 1)
    std = sqrt(variance)
    
    return (s, mean, std)

def main(): 
    for filename in sys.argv[1:]:
        triple = summary(filename)
        print(f"File: {filename} Sum: {triple[0]:.6f} Average: {triple[1]:.6f} Stddev: {triple[2]:.6f}")

if __name__ == "__main__":
    main()
