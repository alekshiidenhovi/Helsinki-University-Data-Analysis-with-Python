#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    
    municipalities = df["Akaa":"Äänekoski"]
    
    columns = ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]
    swedish_speakers = municipalities["Share of Swedish-speakers of the population, %"] > 5
    foreigners = municipalities["Share of foreign citizens of the population, %"] > 5
    
    return municipalities[swedish_speakers][foreigners][columns]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
