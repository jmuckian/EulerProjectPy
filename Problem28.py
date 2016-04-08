"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

ANSWER: 669171001
"""

size = 1001

iterations = (size/2)+1
count = 0
sides = 8
steps = 2

diagonals = []

for i in range(0, iterations):
    if i == 0:
        count += 1
        diagonals.append(count)
    else:
        for j in range(sides * i):
            count += 1
            if (j + 1) % (steps * i) == 0:
                diagonals.append(count)

print sum(diagonals)
            
        
    
    