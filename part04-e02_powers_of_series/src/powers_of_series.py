#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    x_vec = np.ones((1, k))
    values = s.values.reshape((s.size, 1))
    indices = s.index
    
    matrix = values @ x_vec
    df = pd.DataFrame(matrix, columns=range(1, k + 1), index=indices)
    
    i = 1
    while i < df.columns.size + 1:
        df[i] = df[i] ** (i)
        i += 1
    
    return df

def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))

if __name__ == "__main__":
    main()
