"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

i = 999
j = i
largest = 0

while i > 0:
    while j > 0:
        number = str(i * j)
        forward = str(number)
        reverse = ""
        for char in number:
            reverse = char + reverse
        if forward == reverse:
            if largest < i * j:
                largest = i * j
            break
        else:
            j = j - 1
    i = i - 1
    j = i
print largest    