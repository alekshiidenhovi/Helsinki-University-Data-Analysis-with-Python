#!/usr/bin/env python3

import re
from typing import OrderedDict

def file_extensions(filename="src/filenames.txt"):
    with open(filename) as f:
        lines = f.readlines()
        
    L = []
    d = OrderedDict()
        
    for line in lines:
        stripped = line.rstrip("\n")
        pattern = "\w*\.?\w+\.(\w+)"
        snippet = re.findall(pattern, stripped)
        if len(snippet) == 0:
            L.append(stripped)
        else:
            if d.get(snippet[0]) == None:
                d[snippet[0]] = [stripped]
            else:
                d[snippet[0]].append(stripped)
    
    return (L, d)

def main():
    L, d = file_extensions("src/filenames.txt")
    print(f"{len(L)} files with no extension")
    for key in sorted(d.keys()):
        print(f"{key} {len(d[key])}")

if __name__ == "__main__":
    main()
