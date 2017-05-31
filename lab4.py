import operator
from functools import reduce

def gcd(a, b):
    """Reference implementation of finding the
    greatest common denominator of two numbers"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)
    
