#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    "Returns the center coordinates."
    return (a.shape[0] - 1) / 2, (a.shape[1] - 1) / 2  
    
def radial_distance(a):
    # Get the center coordinates
    y, x = center(a)
    
    # Create a matrix with shape (h,w)
    h, w, _ = a.shape
    x_vec = np.arange(w)
    y_vec = np.arange(h)
    matrix = ((x_vec[np.newaxis, :] - x)**2 + (y_vec[:, np.newaxis] - y)**2)**0.5
    
    # Return the matrix
    return matrix

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    if np.max(a) == np.min(a):
        return np.zeros(a.shape)
    
    scaled = (a - a.min()) / np.ptp(a)
    return tmax * scaled + tmin

def radial_mask(a):
    return 1 - scale(radial_distance(a))

def radial_fade(a):
    return a * radial_mask(a)[:, :, np.newaxis]

def main():
    image = plt.imread("src/painting.png")
    f, (ax1, ax2, ax3) = plt.subplots(3, 1)
    
    plt.gray()
    ax1.imshow(image)
    ax2.imshow(radial_mask(image))
    ax3.imshow(radial_fade(image))
    
    plt.show()
    
    
if __name__ == "__main__":
    main()
