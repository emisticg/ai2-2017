from functools import reduce

def fact(n):
    return n > 1 and n * fact(n - 1) or 1

fact(3)  # => 6
fact(7)  # => 5040
