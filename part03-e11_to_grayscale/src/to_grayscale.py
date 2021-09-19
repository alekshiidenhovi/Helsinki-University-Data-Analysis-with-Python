#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_red(image):
    modified = image.copy()
    modified[:, :, [1, 2]] = 0
    return modified

def to_green(image):
    modified = image.copy()
    modified[:, :, [0, 2]] = 0
    return modified

def to_blue(image):
    modified = image.copy()
    modified[:, :, [0, 1]] = 0
    return modified

def to_grayscale(image):
    # painting = plt.imread(image)
    painting = image.copy()
    red = painting[:, :, 0] * 0.2126
    green = painting[:, :, 1] * 0.7152 
    blue = painting[:, :, 2] * 0.0722
    return red + green + blue

def main():
    pic = plt.imread("src/painting.png")
    
    gray = to_grayscale(pic)
    red = to_red(pic)
    green = to_green(pic)
    blue = to_blue(pic)
    
    plt.gray()
    plt.imshow(gray, cmap="gray")

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    ax1.imshow(red)
    ax2.imshow(green)
    ax3.imshow(blue)
    plt.show()
    

if __name__ == "__main__":
    main()
