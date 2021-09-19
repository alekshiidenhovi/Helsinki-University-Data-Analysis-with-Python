#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    # Create the dataframe
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    
    # Replace songs that weren't on the last week's list with nulls.
    cond = (df["LW"] != "New") & (df["LW"] != "Re")
    df = df.where(cond, other=np.nan)
    
    # Change the dtype of pos and lw columns
    df = df.astype({"Pos": float, "LW": float})
    
    # Update the peak values which we can't be sure of
    cond = (df["LW"] > df["Pos"]) & (df["Pos"] == df["Peak Pos"])
    df["Peak Pos"].mask(cond, inplace=True)
    
    # Replace this week's positions with last week's ones, clear LW
    df["Pos"] = df["LW"]
    df.LW = np.nan
    
    # Find missing indices in Pos-column
    all_indices = set(range(1, 41))
    existing_indices = set(df.Pos[pd.notna(df.Pos)])
    missing_indices = list(all_indices - existing_indices)
    
    # Insert missing indices to the Pos-column
    df.Pos[pd.isna(df.Pos)] = missing_indices
    
    # Sort the table by last week's positions
    df.sort_values("Pos", inplace=True)
    
    # Substract one from the Weeks on Chart -column
    df.WoC -= 1
    
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
