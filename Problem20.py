"""
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
ANSWER: 648
"""

n = 100
factorial = 1
sum = 0

while n > 0:
    factorial *= n
    n -= 1

for c in str(factorial):
    sum += int(c)
    
print sum