"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

ANSWER: 872187
"""


baseten = []
palindromic = {}
keys = []


def makebinary(number):
    binary = ""
    place = 2
    r = 0
    while number > 0:
        r = number % place
        if r == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        number -= r
        place *= 2
    return binary

def makereverse(number):
    number = str(number)
    reverse = ""
    for n in number:
        reverse = n + reverse
    return reverse
    
i = 1

while i < 1000000:
    if str(i) == makereverse(i):
        baseten.append(i)
    i += 1
        
for p in baseten:
    binary = makebinary(p)
    if binary == makereverse(binary):
        palindromic[p] = binary
    
for key in palindromic:
    keys.append(key)
    
keys.sort()
print sum(keys)