"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def isprime(number):
    if number % 2 == 0:
        return False
    for x in range(3, int(number**0.5)+1, 2):
        if number % x == 0:
            return False
    return True


primes = []

for i in range(1000, 10000):
    if isprime(i):
        primes.append(i)


low = 4
high = 35

sets = {}

for prime in primes:
    a = 0
    for digit in str(prime):
        a += int(digit)
    if a not in sets:
        sets[a] = [prime]
    else:
        sets[a].append(prime)
        

 
permutations = {}
group = 1

for k in sets:    
    for active in sets[k]:
        temp = [active]
        a = []
        for i in str(active):
            a.append(i)
        a.sort()
        for p in sets[k]:
            b = []
            if p == active:
                continue
            else:
                for i in str(p):
                    b.append(i)
                b.sort()
                if a == b:
                    temp.append(p)
        if len(temp) >= 3:
            permutations[group] = temp
            group += 1
                    
keys = []
for key in permutations:
    keys.append(key)
    
for activekey in keys:
    if activekey not in permutations:
        continue
    for currentkey in keys:
        if currentkey not in permutations:
            continue
        elif activekey == currentkey:
            continue
        elif sum(permutations[activekey]) == sum(permutations[currentkey]) and len(permutations[activekey]) == len(permutations[currentkey]):
            permutations.pop(currentkey)
            

for key in permutations:
    #print key, permutations[key]
    for a in permutations[key]:
        for c in permutations[key]:
            if a == c or a > c:
                continue
            rem = (c - a) % 2
            if rem == 0:
                b = a + ((c - a) / 2.0)
                if b in permutations[key]:
                    print a, b, c

        
#for prime in primes:
    #set = []
    #primesum = 0
    #for i in str(prime):
        #primesum += int(i)
    #for p in primes:
        #workingsum = 0
        #for i in str(p):
            #workingsum += int(i)
        #if primesum == workingsum:
            #set.append(p)
    #print set
    
    
    
    