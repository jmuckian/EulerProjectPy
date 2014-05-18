"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: ""}
tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety", 0: ""}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
hundred = "hundred"
thousand = "onethousand"

number = 1
total = 0

while number < 1000:
    n = str(number)
    places = len(n)
    word = ""
    if places == 1:
        word = ones[int(n[-1])]
    elif places == 2 and int(n[-2]) == 1:
        word = teens[int(n[-2:])]
    elif places == 2 and int(n[-2]) != 1:
        word = tens[int(n[-2])] + ones[int(n[-1])]
    elif places == 3 and int(n[-2]) == 1:
        word = ones[int(n[-3])] + hundred + teens[int(n[-2:])]
    elif places == 3 and int(n[-2]) != 1:
        word = ones[int(n[-3])] + hundred + tens[int(n[-2])] + ones[int(n[-1])]
    if places == 3 and int(n[-2:]) != 0:
        word += "and"
    total += len(word)
    print "%s = %i = %i" % (word, len(word), total)
    number += 1
    

print total + len(thousand)
    