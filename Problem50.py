"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def isprime(number):
    if number == 1:
            return False
    elif number % 2 == 0 and number != 2:
        return False
    else:
        for x in range(3, int(number**0.5)+1, 2):
            if number % x == 0:
                return False
    return True


primes = []
top = 1000000

for x in range(top):
    if isprime(x): primes.append(x)
    

i = 1
longest = []

while i <= len(primes):
    terms = []
    j = i
    while j <= len(primes) and sum(terms) + primes[-j] < top:
        terms.append(primes[-j])
        s = sum(terms)
        if isprime(s) == True and len(terms) > len(longest):
            longest = terms[:]
        j += 1
    i += 1
    
print len(longest), sum(longest)