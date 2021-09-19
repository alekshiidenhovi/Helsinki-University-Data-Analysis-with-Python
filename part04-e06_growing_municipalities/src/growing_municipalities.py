#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    growing = df["Population change from the previous year, %"] > 0
    
    size_all = len(df)
    size_growing = len(df[growing])
    
    return size_growing / size_all

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    municipalities = df["Akaa":"Äänekoski"]
    
    proportion = growing_municipalities(municipalities) * 100
    
    print("Proportion of growing municipalities: {:.1f}%".format(proportion))

if __name__ == "__main__":
    main()
