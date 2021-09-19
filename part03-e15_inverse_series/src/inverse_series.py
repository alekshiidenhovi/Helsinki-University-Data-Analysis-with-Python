#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, index=s.values)

def main():
    values = [1, 2, 3, 3, 7, 4]
    indices = ["a", "b", "c", "d", "e", "f"]
    
    # Original series
    s = pd.Series(values, index=indices)
    print(s)
    
    # Inverse series
    inv = inverse_series(s)
    print(inv)

if __name__ == "__main__":
    main()
