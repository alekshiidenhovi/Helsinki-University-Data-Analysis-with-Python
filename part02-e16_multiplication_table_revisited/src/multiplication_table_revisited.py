#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    rows = np.arange(n)
    columns = np.arange(n).reshape(n, 1)
    return rows * columns

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
