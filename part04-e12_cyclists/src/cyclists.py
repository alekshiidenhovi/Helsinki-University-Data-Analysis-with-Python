#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    rm_rows_columns = df.dropna(how="all").dropna(axis=1, how="all")
    return rm_rows_columns

def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
