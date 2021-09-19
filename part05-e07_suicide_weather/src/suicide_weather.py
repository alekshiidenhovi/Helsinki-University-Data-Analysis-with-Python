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


def suicide_weather():
    # Original dataframes
    fractions = suicide_fractions()
    weather = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", header=0)[0]
    
    # Change weather column name and set is as the index column
    weather = weather.rename(columns={"Country": "country"})
    weather = weather.set_index("country")
    
    # Squeeze weather to a Series
    weather = weather.squeeze()
    
    # Change weather datatype to float
    weather = weather.map(lambda s: s.replace("\u2212", "-"))
    weather = weather.astype(float)
    
    # Common dataframe
    common = pd.merge(fractions, weather, left_index=True, right_index=True)
    
    # Spearman correlation
    spearman = fractions.corr(weather, method="spearman")
    
    # Return tuple length 4
    return (len(fractions), len(weather), len(common), spearman)


def main():
    tuple = suicide_weather()
    print(f"Suicide DataFrame has {tuple[0]} rows")
    print(f"Temperature DataFrame has {tuple[1]} rows")
    print(f"Common DataFrame has {tuple[2]} rows")
    print(f"Spearman correlation: {tuple[3]:.1f}")
    # print(pd.read_html("src/List_of_countries_by_average_yearly_temperature.html")[0])

if __name__ == "__main__":
    main()
