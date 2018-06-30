"""
This program has been written to solve problem 2 on projecteuler.net
author: Jeremiah Lantzer
"""

max_num = 4000000       # even fibonacci numbers under this value
result = []             # stores the fibonacci sequence
past, current = 0, 1    # initializes the first 2 numbers in the sequence
even_sum = 0            # sums the even numbers in the sequence

while past < max_num:
    if past % 2 == 0:
        even_sum += past
    result.append(past)
    past, current = current, past+current

print(result)
print(even_sum)
