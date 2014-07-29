"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

ANSWER: 31626
"""

notamicable = []
isamicable = []

def findDivisors(number):
    i = 2
    divList = [1]
    while i not in divList and i <= number:
        if number % i == 0:
            divList.append(i)
            divList.append(number / i)
        i += 1
    return divList

def amicable(divisors):
    total = 0
    for d in divisors:
        total = total + d
    return total
        

for i in range(10000):
    if i not in notamicable and i not in isamicable:
        a = i
        b = amicable(findDivisors(a))
        c = amicable(findDivisors(b))
        if a == c and not a == b:
            isamicable.append(a)
            isamicable.append(b)
        else:
            notamicable.append(a)
            notamicable.append(b)

print isamicable
t = 0
for v in isamicable:
    t += v
print t
    
#x = 28
#y = amicable(findDivisors(x))
#z = amicable(findDivisors(y))
#print x, y, z                    
    
