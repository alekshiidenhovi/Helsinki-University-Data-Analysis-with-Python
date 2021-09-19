#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    data = [["United Kingdom", np.nan, None],
            ["Finland", 1917, "Niinistö"],
            ["USA", 1776, "Trump"],
            ["Sweden", 1523, None],
            ["Germany", np.nan, "Steinmeier"],
            ["Russia", 1992, "Putin"]]
    cols = ["State", "Year of independence", "President"]
    
    return pd.DataFrame(data, columns=cols).set_index("State")

def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
