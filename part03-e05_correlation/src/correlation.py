#!/usr/bin/env python3

from scipy.stats import pearsonr
import numpy as np

def calc_corr(dataframe, x, y):
    return pearsonr(dataframe[:, x], dataframe[:, y])[0]

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    df = load()
    return calc_corr(df, 0, 2)

def correlations():
    df = load()
    return np.corrcoef(df, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
