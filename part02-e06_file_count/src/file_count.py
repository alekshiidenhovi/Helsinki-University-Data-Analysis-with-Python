#!/usr/bin/env python3

import sys
import re
from functools import reduce

def file_count(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        
    line_count = len(lines)
    
    character_count = 0
    words = []
    for line in lines:
        words += line.split()
        character_count += len(line)
    
    word_count = len(words)
    
    return (line_count, word_count, character_count)
    

def main():
    for filename in sys.argv[1:]:
        toStr = map(str, file_count(filename))
        line = "\t".join(toStr) + f"\t{filename}"
        print(line)

if __name__ == "__main__":
    main()
