#!/usr/bin/env python3

import re



def file_listing(filename="src/listing.txt"):
    L = []
    with open(filename, "r") as f:
        for line in f:
            pattern = "^[rwdx-]{10}\s\d\s[a-z]+\shyad-all\s+(\d+)\s([A-Z][a-z]{2})\s+(\d+)\s(\d{2}):(\d{2})\s([\w\.-]+)$"
            snippet = re.findall(pattern, line)[0]
            snippet = (int(snippet[0]), snippet[1], int(snippet[2]), int(snippet[3]), int(snippet[4]), snippet[5])
            L.append(snippet)
        
    return L

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
