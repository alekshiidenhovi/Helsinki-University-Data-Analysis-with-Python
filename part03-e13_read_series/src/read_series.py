#!/usr/bin/env python3

import pandas as pd

def read_series():
    inputs = "continue"
    indices = []
    values = []
    
    while inputs != "":
        inputs= input("Give some input: ")
        if len(inputs.split()) == 1:
            raise Exception
        elif len(inputs.split()) == 0:
            continue
        else:
            output = inputs.split()
            index, value = output[0], output[1]
            indices.append(index)
            values.append(value)
        
    return pd.Series(values, index=indices)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
