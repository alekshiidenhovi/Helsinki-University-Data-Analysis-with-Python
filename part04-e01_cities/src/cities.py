#!/usr/bin/env python3

import pandas as pd
import numpy as np

def cities():
    pop_list = np.array([643272, 279044, 231853, 223027, 201810])
    area_list = np.array([715.48, 528.03, 689.59, 240.35, 3817.52])
    indices = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    
    return pd.DataFrame({"Population": pop_list, "Total area": area_list}, index=indices)
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
