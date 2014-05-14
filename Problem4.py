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