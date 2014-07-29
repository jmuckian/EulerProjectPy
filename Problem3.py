"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

ANSWER: 6857
"""

number = 600851475143

i = 2

while number >= i:
    if number % i == 0:
        print i,
        number = number / i
        i = 2
    else:
        i = i + 1
