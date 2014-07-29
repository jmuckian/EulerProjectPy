"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

ANSWER: 871198282
"""

import string

source = open("./files/names.txt", "r")
rawnames = source.read()
source.close()
rawnames = rawnames.replace('"','')
names = rawnames.split(',')
names.sort()
totalsum = 0

letterValues = {}

for i in range(len(string.uppercase)):
    letterValues[string.uppercase[i]] = i + 1
    
    

def sumName(name):
    total = 0
    for a in range(len(name)):
        total += letterValues[name[a]]
    return total
        
        
for i in range(len(names)):
    totalsum += sumName(names[i]) * (i + 1)
    
print totalsum
    


