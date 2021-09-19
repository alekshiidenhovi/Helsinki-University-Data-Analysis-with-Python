#!/usr/bin/env python3

def reverse_dictionary(d):
    rev = {}
    for key, values in d.items():
        for value in values:
            if rev.get(value) != None:
                rev[value].append(key)
            else:
                rev[value] = [key]
    
    return rev
        

def main():
    d = {"syödä": ["eat"]}

if __name__ == "__main__":
    main()
