#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    return pd.DataFrame(df[1:312])
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
