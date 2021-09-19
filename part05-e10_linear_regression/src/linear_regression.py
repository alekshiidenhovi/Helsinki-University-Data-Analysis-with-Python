#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    # Initialize linear regression model
    model = LinearRegression()
    
    # Fit the arrays in the model
    model.fit(x[:, np.newaxis], y)
    
    # Return the slope and y-intercept
    return model.coef_[0], model.intercept_
    
def main():
    x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y1 = np.array([3, 5, 8.5, 12, 14, 17, 22, 24, 26, 28])
    
    model_1 = fit_line(x1, y1)
    slope = model_1[0]
    intercept = model_1[1]
    
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    
    plt.plot(x1, slope * x1 + intercept)
    plt.plot(x1, y1, "go")
    # plt.plot(np.vstack([x1, x1]), np.vstack([y1, slope * x1 + intercept]))
    plt.show()
    
if __name__ == "__main__":
    main()
