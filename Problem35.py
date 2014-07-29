"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

ANSWER: 55
"""

n = 197
circulars = [2]

def rotate(numbers):
    x = []
    for n in range(len(str(numbers))):
        x.append(str(numbers)[n])
    y = x.pop()
    x.insert(0, y)
    return int("".join(x))

def isprime(number):
    for x in range(3, int(number**0.5)+1, 2):
        if number % x == 0:
            return False
    return True
    
def iscircular(number):
    primes = []
    for i in range(len(str(number))):
        if number % 2 == 0:
            return False
        elif isprime(number) == False:
            return False
        else:
            primes.append(number)
            number = rotate(number)
    for p in primes:
        if p not in circulars: circulars.append(p)



for i in range(3, 1000000, 2):
    if i not in circulars: iscircular(i)
    
print circulars
print len(circulars)
    