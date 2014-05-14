total = 0
n = 2

while total < 10001:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime == True:
        total += 1
        print n
    n += 1
    
    