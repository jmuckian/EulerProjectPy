terms = []

a = 2
b = 100


while a <= b:
    i = 2
    j = 100
    
    while i <= j:
        if a**i not in terms: terms.append(a**i)
        i += 1
    a += 1

print len(terms)    
print terms