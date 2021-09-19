#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    # Pick the column to be sorted by
    col = a[:, c]

    # Take the unique values of a and counts of those values
    values, counts = np.unique(col, return_counts=True)
    
    # Get the indices of the rows that are in the sorted order
    counts_by_freq = np.flip(np.argsort(counts))
    sorted_values = values[counts_by_freq]
    
    first = True
    indices = np.array([])
    for value in sorted_values:
        if first:
            indices = np.argwhere(col == value)
            first = False
        else:
            indices = np.concatenate((indices, np.argwhere(col == value)))
            
    flatten = indices.reshape(indices.size)
    return a[flatten]


def main():
    np.random.seed(100)
    arr = np.random.randint(0, 10, (10, 10))
    # count = np.bincount(arr)
    # print(count)
    print(arr)
    print(most_frequent_first(arr, -1))

if __name__ == "__main__":
    main()
