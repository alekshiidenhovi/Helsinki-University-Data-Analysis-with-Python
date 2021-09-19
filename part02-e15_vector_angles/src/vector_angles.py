#!/usr/bin/env python3

import numpy as np
import scipy.linalg
from math import pi

def vector_angles(X, Y):
    x_len = np.sqrt(np.sum(X**2, axis=1))
    y_len= np.sqrt(np.sum(Y**2, axis=1))
    
    upper = np.sum(X*Y, axis=1)
    cos_values = upper / (x_len * y_len)
    clipped = np.clip(cos_values, a_min=-1, a_max=1)
    
    return np.arccos(clipped) * 360 / (2*pi)

def main():
    shape = (3, 4)
    X = np.random.randint(0, 10, shape)
    Y = np.random.randint(0, 10, shape)
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
