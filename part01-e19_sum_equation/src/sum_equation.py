#!/usr/bin/env python3

def sum_equation(L):
    if len(L) != 0:
        return " + ".join(map(str, L)) + f" = {sum(L)}"
    else:
        return "0 = 0"

def main():
    L = [1, 5, 3, 6]
    print(sum_equation(L))

if __name__ == "__main__":
    main()
