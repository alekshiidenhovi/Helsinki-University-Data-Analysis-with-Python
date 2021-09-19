#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x = a[:,0]
    y = a[:,1]
    color = a[:,2]
    size = a[:,3]
    
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x, y)
    ax2.scatter(x, y, c=color, s=size)
    
    plt.show()

def main():
    a = np.array([[1, 2, 3, 4, 5, 7], [2, 4, 1, 3, 9, 4]])
    subfigures(a)
    

if __name__ == "__main__":
    main()
