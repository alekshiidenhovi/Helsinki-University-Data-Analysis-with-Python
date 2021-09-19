#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    # Original datafram
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    
    # Dataframe grouped by the publisher
    grouped = df.groupby("Publisher")
    
    # Get the sums of the WoC per publisher 
    sums = grouped.WoC.sum()
    
    # Get the best publisher
    best = sums.idxmax()
    
    # Get singles of that publisher
    return df[df.Publisher == best]
    

def main():
    df = best_record_company()
    print(df)
    

if __name__ == "__main__":
    main()
