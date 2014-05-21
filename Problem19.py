"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Julian dates for January 1, 1901 and January 1, 2001
start = 2415385
end = 2451910

years = 100
months = 12
monthDays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
leapDays = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

dateRange = end - start

total = 0
sundays = 0

for year in range(years):
    for i in range(months):
        a = i + 1
        if (year + 1) % 4 == 0: 
            for j in range(leapDays[a]):
                total += 1
                if j == 0 and total % 7 == 6:
                    sundays += 1
        else:
            for j in range(monthDays[a]):
                total += 1
                if j == 0 and total % 7 == 6:
                    sundays += 1                
                
print sundays
        
        

