#!/usr/bin/env python3

def triple(num):
    return num * 3

def square(num):
    return num**2

def main():    
    for i in range(1, 11):
        tri = triple(i)
        sq = square(i)
        if tri >= sq:
            print(f"triple({i})=={tri} square({i})=={sq}")
        else:
            break
        i += 1

if __name__ == "__main__":
    main()
