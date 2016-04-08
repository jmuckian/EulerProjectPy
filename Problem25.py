"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

ANSWER: 4782
"""

numbers = [0, 1]


def findfib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return findfib(number - 1) + findfib(number -2)

def fibonacci(a, b):
    return a + b

i = 0

while len(str(numbers[-1])) < 1000:
    numbers.append(fibonacci(numbers[i], numbers[i + 1]))
    i += 1
    
print numbers[-1]
print len(str(numbers[-1]))

#print numbers
print len(numbers) - 1
