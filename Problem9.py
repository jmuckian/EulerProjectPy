import math



def pythagorean(a, b):
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    return c


a = 3
b = 4
c = pythagorean(a, b)

while a + b + c < 1001:
    while a + b + c < 1001:
        if a + b + c == 1000:
            print a, b, c, a * b * c
        b += 1
        c = pythagorean(a, b)
    a += 1
    b = a + 1
    c = pythagorean(a, b)
    
