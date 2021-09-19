#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    modified = df.replace(["New", "Re"], np.nan).dropna(how="any")
    condition = modified["Pos"] > modified["LW"].astype(int)
    
    return modified[condition]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
