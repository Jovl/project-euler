"""
This program has been written to solve problem 12 on projecteuler.net
author: Jeremiah Lantzer
"""

import math

counter = 0
divisibles = 0


def tri_number(amount):
    triangle_number = 0
    for j in range(1, amount+1):
        triangle_number += j
    return triangle_number  # returns a certain triangle number given a positional number (1st, 2nd, 3rd)


def gen_divs(nat_sum):
    divisors = []
    for i in range(1, int(nat_sum**0.5)+1):
        if nat_sum % i == 0:
            yield i
            if i is not nat_sum/i:
                divisors.insert(0, nat_sum / i)
    for div in divisors:
        yield div

def divs_actual(n):
    return [div for div in gen_divs(n)]

while divisibles < 500:
    counter += 1
    nums = tri_number(counter)
    divs = divs_actual(nums)
    divisibles = len(divs)

print("Final: ", nums)
print("Divisors: ", divisibles)

# print("Amount of divisors for ", nat_sum, ": ", divisibles)

