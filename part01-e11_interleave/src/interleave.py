#!/usr/bin/env python3

def interleave(*lists):
    L = []
    
    for zipped in list(zip(*lists)):
            for element in zipped:
                L.append(element)
            
    return L

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
