#!/usr/bin/env python3

def extract_numbers(s):
    L = []
    words = s.split()
    for word in words:
        try:
            x = int(word)
            L.append(x)
        except:
            try:
                x = float(word)
                L.append(x)
            except:
                continue
        
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
