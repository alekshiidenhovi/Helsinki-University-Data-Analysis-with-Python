#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


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


def cycling_weather():
    # Create the dataframes
    cyclists = split_date_continues()
    weather = pd.read_csv("src/kumpula-weather-2017.csv")
    
    # Restrict the cycling data to 2017 and drop the hour column
    restrict = cyclists.Year == 2017
    cyclists = cyclists[restrict].drop(columns=["Hour"])
    
    # Get the daily cycling sums, after which reset the index
    cyclists = cyclists.groupby(["Year", "Month", "Day"]).sum()
    cyclists = cyclists.reset_index()
    
    # Name the columns by which the dataframes will be merged
    col_c = ["Year", "Month", "Day"]
    col_w = ["Year", "m", "d"]
    
    # Merge the dataframes by year, month and day
    merged = pd.merge(cyclists, weather, left_on=col_c, right_on=col_w)
    
    # Remove the obsolete columns
    obsolete = ["m", "d", "Time", "Time zone"]
    clean_merge = merged.drop(columns=obsolete)
    
    return clean_merge


def cycling_weather_continues(station):
    # Merged dataframe
    df = cycling_weather().fillna(method="ffill")
    
    # X and y variables
    precipitation = df["Precipitation amount (mm)"]
    snow = df["Snow depth (cm)"]
    air = df["Air temperature (degC)"]
    
    X = np.vstack([precipitation, snow, air]).T
    y = df[station]
    
    # Create the linear regression model and fit the model to the data
    model = LinearRegression()
    model.fit(X, y)
    
    return (model.coef_, model.score(X, y))


def main():
    station = "Ratapihantie"
    coefs, score = cycling_weather_continues(station)
    
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coefs[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coefs[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coefs[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
