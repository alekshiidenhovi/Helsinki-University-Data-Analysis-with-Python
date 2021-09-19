#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    snippets = re.findall(r'[\[\s]([+-]?\b\d+)[\]\s]', s)
    result = list(map(int, snippets)) 
    return result

def main():
    snippet = "  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(snippet))

if __name__ == "__main__":
    main()

