#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    # Helper function to clean up names
    def clean(name):
        first, second = name.split()
        if first.endswith(","):
            stripped = first.rstrip(",")
            return f"{second.capitalize()} {stripped.capitalize()}"
        else:
            return f"{first.capitalize()} {second.capitalize()}"
        
    
    # Create the dataframe
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    print(df.dtypes)
    
    # Clean the columns
    df.President = df.President.map(clean)
    df.Start = df.Start.str.replace(r"\s\w*", "")
    df.Last = df.Last.str.replace("-", "NaN")
    df.Seasons = df.Seasons.str.replace("two", "2")
    df["Vice-president"] = df["Vice-president"].map(clean)
    
    # Change the datatypes
    df = df.astype({"President":object, "Start":int, "Last":float, "Seasons":int, "Vice-president":object})

    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
