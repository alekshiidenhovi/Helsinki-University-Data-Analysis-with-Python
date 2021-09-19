#!/usr/bin/env python3

def word_frequencies(filename="src/alice.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()
    
    d = {}
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
            if d.get(word) != None:
                d[word] += 1
            else: 
                d[word] = 1
        
    
    return d

def main():
    d = word_frequencies()
    for line in d:
        print(line, d[line])

if __name__ == "__main__":
    main()
