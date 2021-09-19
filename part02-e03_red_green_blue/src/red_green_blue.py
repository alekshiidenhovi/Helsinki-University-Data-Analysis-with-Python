#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename) as f:
        lines = f.readlines()
    
    result = []
    for line in lines:
        pattern = "(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(\w+\s?\w*\s?\w*)"
        snippet = re.findall(pattern, line)[0]
        new_tuple = "\t".join(snippet).rstrip("\n")
        result.append(new_tuple)
    
    return result


def main():
    lines = red_green_blue()
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()



