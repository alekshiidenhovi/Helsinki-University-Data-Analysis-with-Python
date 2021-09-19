#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    squared = a**2
    euclidean = squared.sum(axis=1)
    
    return np.sqrt(euclidean)

def main():
    a = np.random.randint(0, 10, (3, 4))
    print(a)
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
