#!/usr/bin/env python3

class Rational(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.value = first / second
    
    def __add__(self, other):
        numerator = self.first * other.second + self.second * other.first
        denominator = self.second * other.second
        return Rational(numerator, denominator)
    
    def __sub__(self, other):
        numerator = self.first * other.second - self.second * other.first
        denominator = self.second * other.second
        return Rational(numerator, denominator)
    
    def __mul__(self, other):
        return Rational(self.first*other.first, self.second*other.second)
    
    def __truediv__(self, other):
        return Rational(self.first*other.second, self.second*other.first)
    
    def __str__(self):
        return f"{self.first}/{self.second}"
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __lt__(self, other):
        return self.value < other.value

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
