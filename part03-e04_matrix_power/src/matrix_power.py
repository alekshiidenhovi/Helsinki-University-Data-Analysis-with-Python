#!/usr/bin/env python3

from functools import reduce
import numpy as np
from numpy.linalg import inv

def matrix_power(a, n):
    m = a.shape[0]
    if n > 0:
        return reduce(lambda x,y: x @ y, (a for b in range(n)))
    elif n == 0:
        return np.eye(m)
    else: 
        return reduce(lambda x,y: x @ y, (inv(a) for b in range(-n)))

def main():
    mat = np.array([[1, 6], [1, 4]])
    print(matrix_power(mat, -2))
    print(matrix_power(mat, 0))
    print(matrix_power(mat, 3))

if __name__ == "__main__":
    main()
