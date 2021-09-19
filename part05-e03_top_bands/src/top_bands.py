#!/usr/bin/env python3

import pandas as pd

def top_bands():
    # Create the dataframes
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    uk = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    
    # Make the bands.Band column upper case
    bands.Band = bands.Band.str.upper()
    
    # Merge the two dataframes together
    merged = pd.merge(uk, bands, left_on=["Artist"], right_on=["Band"])
    
    return merged

def main():
    df = top_bands()
    print(df)

if __name__ == "__main__":
    main()
