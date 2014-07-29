"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

ANSWER: 443839
"""

fives = []
total = 0

def getTerms(number):
    i = 0
    terms = []
    while i < len(str(number)):
        terms.append(int(str(number)[i]))
        i += 1
    return terms
    
def sumTerms(list):
    total = 0
    for i in list:
        total += i**5
    return total
        

for x in xrange(2, 1000000):
    
    y = sumTerms(getTerms(x))
    if x == y: fives.append(x)
    
for x in fives:
    total += x

print fives    
print total
    