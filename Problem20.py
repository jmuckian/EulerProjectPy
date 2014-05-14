n = 100
factorial = 1
sum = 0

while n > 0:
    factorial *= n
    n -= 1

for c in str(factorial):
    sum += int(c)
    
print sum