"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

ANSWER: 40730
"""

from math import factorial



def breakdown(number):
    l = []
    for i in range(len(str(number))):
        l.append(int(str(number)[i]))
    return l
        
def sumFactors(list):
    x = 0
    for i in digits:
        x += factorial(i)
    return x



numbers = []

for n in xrange(3, 1000000):
    digits = breakdown(n)
    if n == sumFactors(digits):
        numbers.append(n)
        
print sum(numbers), numbers
    
