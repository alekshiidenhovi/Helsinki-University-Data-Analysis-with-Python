#!/usr/bin/env python3

import pandas as pd


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

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
