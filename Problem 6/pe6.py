"""
This program has been written to solve problem 6 on projecteuler.net
author: Jeremiah Lantzer
"""

import math

nat_num_amount = 100
num_sum_2 = 0           # will hold the sum of the natural numbers squared
nat_nums = 0            # wil hold the sum of the natural numbers

for i in range(1, nat_num_amount + 1):
    num_sum_2 += math.pow(i, 2)
    nat_nums += i

nat_nums_2 = math.pow(nat_nums, 2)
print("Sum of the squared natural numbers: " + str(num_sum_2))
print("Sum of the squared natural numbers: " + str(nat_nums_2))
print("Difference: " + str(nat_nums_2 - num_sum_2))
