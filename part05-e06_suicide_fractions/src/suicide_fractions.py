#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    # Original dataframe
    df = pd.read_csv("src/who_suicide_statistics.csv", index_col="country")
    
    # Count the fractions by row
    df["fraction"] = df.suicides_no / df.population
    
    # Group by country
    grouped = df.groupby("country")
    
    # Return the mean of the fractions
    return grouped.fraction.mean()

def main():
    df = suicide_fractions()
    print(df)

if __name__ == "__main__":
    main()
