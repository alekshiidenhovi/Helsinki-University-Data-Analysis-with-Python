#!/usr/bin/env python3

import pandas as pd


def bicycle_timeseries():
    # Original dataframe
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    
    # Clean empty rows and columns
    df = df.dropna(how="all").dropna(how="all", axis=1)
    
    # Create the conversion dictionaries
    days = {"ma":"Mon", "ti":"Tue", "ke":"Wed", "to":"Thu", "pe":"Fri", "la":"Sat", "su":"Sun"}
    months = {"tammi":1, "helmi":2, "maalis":3, "huhti":4, "touko":5, "kesä":6, "heinä":7, "elo":8, "syys":9, "loka":10, "marras":11, "joulu":12}
    
    # Helper function to create the hour column
    def time_to_hour(time):
        hour = time.split(":")[0]
        return int(hour)    

    # Split the Päivämäärä to five seperate columns and rename them
    date = df.Päivämäärä.str.split(expand=True)
    date.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
        
    # Clean the data
    date.Weekday = date.Weekday.map(days)
    date.Day = date.Day.map(int)
    date.Month = date.Month.map(months)
    date.Year = date.Year.map(int)
    date.Hour = date.Hour.map(time_to_hour)
    
    # Concatenate the new date column and the original dataframe
    og_no_date = df.drop(columns=["Päivämäärä"])
    cleaned = pd.concat([date, og_no_date], axis=1)
    
    # Make a new column Date from Year, Month and Day columns
    cleaned["DateTimeIndex"] = pd.to_datetime(cleaned[["Year", "Month", "Day", "Hour"]])
    
    # Drop the obsolete columns and set Date column as the index
    cleaned = cleaned.drop(columns=["Year", "Month", "Day", "Hour", "Weekday"])
    cleaned = cleaned.set_index("DateTimeIndex")
    
    return cleaned


def main():
    df = bicycle_timeseries()
    print(df)

if __name__ == "__main__":
    main()
