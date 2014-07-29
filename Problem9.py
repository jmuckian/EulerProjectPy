"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

ANSWER: 31875000
"""

import math


def pythagorean(a, b):
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    return c


a = 3
b = 4
c = pythagorean(a, b)

while a + b + c < 1001:
    while a + b + c < 1001:
        if a + b + c == 1000:
            print a, b, c, a * b * c
        b += 1
        c = pythagorean(a, b)
    a += 1
    b = a + 1
    c = pythagorean(a, b)
    
