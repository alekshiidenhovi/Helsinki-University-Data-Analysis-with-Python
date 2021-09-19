#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    return a[a[:, 1] > a[:, -2]]
    
def main():
    print(column_comparison(np.array([[1, 2, 3, 4], [4, 3, 2, 1], [0, 0, 0 ,0]])))
    print(np.array([[1, 2, 3, 4], [4, 3, 2, 1], [0, 0, 0 ,0]]).shape)

if __name__ == "__main__":
    main()
