#!/usr/bin/env python3

def transform(s1, s2):
    first_list = map(int, s1.split())
    second_list = map(int, s2.split())
    
    zipped = list(zip(first_list, second_list))
    final_list = [a * b for a, b in zipped]
    
    return final_list

def main():
    s1 = "1 51 12 4"
    s2 = "4 6 99 2"
    print(transform(s1, s2))

if __name__ == "__main__":
    main()
