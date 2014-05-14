sum_squared = 0
squared_sum = 0

for i in range(1, 101):
    sum_squared += i**2
    squared_sum += i
squared_sum = squared_sum**2

print squared_sum - sum_squared
