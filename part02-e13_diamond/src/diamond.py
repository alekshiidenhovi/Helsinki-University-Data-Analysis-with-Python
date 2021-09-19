#!/usr/bin/env python3

import numpy as np

def diamond(n):
    identity = np.eye(n, dtype=int)
    upper = np.concatenate([identity[::-1], identity[:,1:]], axis=1)
    complete = np.concatenate([upper, upper[::-1][1:]], axis=0)
    
        
    return complete

def main():
    print(diamond(1))
    print(diamond(5))

if __name__ == "__main__":
    main()
