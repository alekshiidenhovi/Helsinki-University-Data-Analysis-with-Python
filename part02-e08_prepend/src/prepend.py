#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, param):
        self.start = param
    
    def write(self, s):
        print(self.start + s)
        

def main():
    i = Prepend("lol")
    i.write("xd")

if __name__ == "__main__":
    main()
