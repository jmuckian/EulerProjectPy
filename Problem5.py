n = 20
divisible = False

while divisible == False:
    n += 20
    divisible = True
    for i in range(1, 21):
        if n % i != 0:
            divisible = False
            continue
print n
