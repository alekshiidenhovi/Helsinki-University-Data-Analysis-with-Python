#!/usr/bin/env python3

def detect_ranges(L):
    # Initialize lists and other helper variables
    sorted_list = sorted(L)
    arr = []
    length = len(sorted_list)
    i = 0
    
    # Loop over the list
    while i + 1 < length:
        if sorted_list[i] + 1 == sorted_list[i+1]:
            start = sorted_list[i]
            end = start + 2
            i += 1
            
            while i + 1 < length and sorted_list[i] + 1 == sorted_list[i+1]:
                end += 1
                i += 1
                
            arr.append((start, end))
            i += 1
        else:
            arr.append(sorted_list[i])
            i += 1
    
    # If i == last index of L, then add the last element to arr.
    if i + 1 == length:
        arr.append(sorted_list[i])
        
    return arr

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    M = [-4, -2, 0, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(detect_ranges(M))
    print(result)

if __name__ == "__main__":
    main()
