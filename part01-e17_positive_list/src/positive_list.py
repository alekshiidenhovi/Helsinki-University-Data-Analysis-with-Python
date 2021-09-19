#!/usr/bin/env python3

def positive_list(L):
    return list(filter(lambda x: x > 0, L))

def main():
    L = [0, 4, 7, -2, 3]
    print(positive_list(L))

if __name__ == "__main__":
    main()
