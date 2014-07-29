"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

primes = [2]
n = 3
sum = 0

while n < 2000000:
    isprime = True
    for prime in primes:
        if n % prime == 0:
            isprime = False
            break
    if isprime == True:
        primes.append(n)
    isprime = True
    n += 2

for prime in primes:
    sum += prime
    
print sum