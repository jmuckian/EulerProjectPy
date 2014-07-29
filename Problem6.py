"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

ANSWER: 25164150
"""

sum_squared = 0
squared_sum = 0

for i in range(1, 101):
    sum_squared += i**2
    squared_sum += i
squared_sum = squared_sum**2

print squared_sum - sum_squared
