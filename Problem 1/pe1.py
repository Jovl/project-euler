"""
This program has been written to solve problem 1 on projecteuler.net
author: Jeremiah Lantzer
"""

start_num = 1000    # find the natural numbers below this number who are multiples of 3 or 5
sum_multiples = 0   # sum will store the total of the numbers divisible by 3 and 5

for i in range(start_num):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        sum_multiples += i

print(sum_multiples)
