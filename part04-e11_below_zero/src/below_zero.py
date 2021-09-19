#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    under = df["Air temperature (degC)"] < 0
    return len(df[under])

def main():
    under = below_zero()
    print(f"Number of days below zero: {under}")
    
if __name__ == "__main__":
    main()
