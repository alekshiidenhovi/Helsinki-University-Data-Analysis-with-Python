#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    length = a.shape[1] // 2
    mask = np.sum(a[:, :length], axis=1) > np.sum(a[:, length:], axis=1)
    return a[mask]

def main():
    arr = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
    print(first_half_second_half(arr))

if __name__ == "__main__":
    main()
