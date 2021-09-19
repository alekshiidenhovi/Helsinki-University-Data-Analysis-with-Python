#!/usr/bin/env python3

def find_matching(L, pattern):
    indices = []
    for idx, value in enumerate(L):
        if pattern in value:
            indices.append(idx)
            
    return indices

def main():
    indices = find_matching(["english", "finnish", "book", "cat", "ticklish"], "ish")
    print(indices)

if __name__ == "__main__":
    main()
