"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

ANSWER: 104743
"""

total = 0
n = 2

while total < 10001:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime == True:
        total += 1
    n += 1
    
print n