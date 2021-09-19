#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model


def coefficient_of_determination():
    # Original dataframe
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    
    # Variables X and y
    X = df.drop(columns=["Y"])
    y = df.Y

    # Linear regression model
    model = linear_model.LinearRegression().fit(X, y)
    
    # Determination score list
    scores = [model.score(X, y)]
    
    # Loop over columns and get their specific determinations
    for feature in X:
        x = df[[feature]]
        model.fit(x, y)
        scores.append(model.score(x, y))
        
    return scores
        
    
def main():
    det = coefficient_of_determination()
    for i, model in enumerate(det):
        if i == 0:
            print(f"R2-score with feature(s) X: {model:.3f}")
        else: 
            print(f"R2-score with feature(s) X{i}: {model:.3f}")

if __name__ == "__main__":
    main()
