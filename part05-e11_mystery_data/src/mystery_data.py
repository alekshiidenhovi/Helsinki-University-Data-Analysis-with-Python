#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
    # Original dataframe
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    
    # Variables x and y
    x = df.drop(columns=["Y"])
    y = df.Y
    
    # Linear regression model
    model = LinearRegression(fit_intercept=False)
    
    # Fit the model in the training data
    model.fit(x, y)
    
    return model.coef_

def main():
    coefficients = mystery_data()
    print(f"Coefficient of X1 is {coefficients[0]}")
    print(f"Coefficient of X2 is {coefficients[1]}")
    print(f"Coefficient of X3 is {coefficients[2]}")
    print(f"Coefficient of X4 is {coefficients[3]}")
    print(f"Coefficient of X5 is {coefficients[4]}")

if __name__ == "__main__":
    main()
