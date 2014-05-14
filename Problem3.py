number = 600851475143

i = 2

while number >= i:
    if number % i == 0:
        print i,
        number = number / i
        i = 2
    else:
        i = i + 1
