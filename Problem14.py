longest = 0
most_terms = 0
i = 2

while i < 1000001:
    print i
    n = i
    terms = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        terms += 1
    if terms > most_terms:
        most_terms = terms
        longest = i
    i += 1

print longest, most_terms
