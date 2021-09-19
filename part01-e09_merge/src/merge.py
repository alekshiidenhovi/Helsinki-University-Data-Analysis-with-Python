#!/usr/bin/env python3

def merge(L1, L2):
    first_len = len(L1)
    second_len = len(L2)
    
    i = 0
    j = 0
    
    L = []
    
    while i < first_len or j < second_len:
        if i == first_len:
            L.extend(L2[j:])
            break
        elif j == second_len:
            L.extend(L1[i:])
            break
        else:
            if L1[i] < L2[j]:
                L.append(L1[i])
                i += 1
            else:
                L.append(L2[j])
                j += 1
    
    return L
    
    

def main():
    L1 = [1, 3, 6, 8, 9, 14]
    L2 = [4, 6, 7, 11]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
