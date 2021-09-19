#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return max(df["Snow depth (cm)"])

def main():
    snow = snow_depth()
    print(f"Max snow depth: {snow:.1f}")

if __name__ == "__main__":
    main()
