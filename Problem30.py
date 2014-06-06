fives = []
total = 0

def getTerms(number):
    i = 0
    terms = []
    while i < len(str(number)):
        terms.append(int(str(number)[i]))
        i += 1
    return terms
    
def sumTerms(list):
    total = 0
    for i in list:
        total += i**5
    return total
        

for x in xrange(2, 1000000):
    
    y = sumTerms(getTerms(x))
    if x == y: fives.append(x)
    
for x in fives:
    total += x

print fives    
print total
    