#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def split_date(df):
    # Remove the empty lines
    df = df.dropna(how="all")
    
    # Create a new dateframe for only the date and time
    date = df.Päivämäärä.str.split(expand=True)
    
    # Change column names
    date.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    
    # Create the conversion dictionaries
    days = {"ma":"Mon", "ti":"Tue", "ke":"Wed", "to":"Thu", "pe":"Fri", "la":"Sat", "su":"Sun"}
    months = {"tammi":1, "helmi":2, "maalis":3, "huhti":4, "touko":5, "kesä":6, "heinä":7, "elo":8, "syys":9, "loka":10, "marras":11, "joulu":12}
    
    # Function do to time conversion to hours
    def time_to_hour(time):
        string = str(time)
        hour_part = string.split(":")[0]
        return int(hour_part)
    
    # Convert columns
    date.Weekday = date.Weekday.map(days)
    date.Day = date.Day.map(int)
    date.Month = date.Month.map(months)
    date.Year = date.Year.map(int)
    date.Hour = date.Hour.map(time_to_hour)
    
    return date

def split_date_continues():
    # Get the original dataframe
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    
    # Remove empty rows and columns
    df = df.dropna(how="all", axis=1).dropna(how="all")
    
    # Get the dateframe which has the date split into multiple columns
    date = split_date(df)
    
    # Drop the Päivämäärä column
    pruned = df.drop(columns=["Päivämäärä"])
    
    return pd.concat([date, pruned], axis=1)

def cyclists_per_day():
    # Get the original dataframe
    df = split_date_continues()
    
    # Drop the Hour and Weekday columns
    df = df.drop(columns=["Hour", "Weekday"])
    
    # Group by year, month and day
    grouped = df.groupby(["Year", "Month", "Day"]).sum()
    
    return grouped
    
def main():
    # Original dataframe
    df = cyclists_per_day()
    
    # Dataframe of August 2017
    august_2017 = df.loc[2017, 8, :]
    print(august_2017)
    
    # Helper array
    arr = np.array(range(1, 32))
    
    # Plot the dataframe with matplotlib
    plt.plot(arr, august_2017)
    plt.xticks(arr)
    plt.show()

if __name__ == "__main__":
    main()
