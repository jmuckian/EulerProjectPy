"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

ANSWER: 232792560
"""

n = 20
divisible = False

while divisible == False:
    n += 20
    divisible = True
    for i in range(1, 21):
        if n % i != 0:
            divisible = False
            continue
print n
